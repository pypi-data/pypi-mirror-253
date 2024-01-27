import os
import ast
import subprocess
import psycopg2
import datetime
from pathlib import Path

from psycopg2 import OperationalError
from omni.pro import redis
from omni.pro.config import Config
from omni.pro.logger import configure_logger

logger = configure_logger(name=__name__)


class AlembicCheckMigrations:

    def __init__(self, app_path):
        self.alembic_version_files = self.get_alembic_version_files_id()
        self.redis_manager = redis.get_redis_manager()
        self.tenants = self.redis_manager.get_tenant_codes()
        self.app_path = app_path

    def get_postgres_config(self, service_id, tenant_code):
        postres_config = self.redis_manager.get_postgres_config(Config.SERVICE_ID, tenant_code)
        host, port, user, password, name = postres_config.values()
        if all([host, port, user, password, name]):
            return host, port, user, password, name
        logger.error(f"Postgres config not found for tenant: {tenant_code}")

    def get_alembic_version(self, host, port, user, password, dbname):
        try:
            conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbname)
        except OperationalError as e:
            logger.error(f"Error de conexión a la base de datos: {e}")
            raise e

        try:
            cursor = conn.cursor()

            # Verifica si la tabla existe
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE schemaname = 'public' AND tablename  = 'alembic_version'
                );
            """)
            if not cursor.fetchone()[0]:
                logger.warning("La tabla 'public.alembic_version' no existe en la base de datos.")
                return None

            # Recupera el número de versión
            cursor.execute("SELECT version_num FROM public.alembic_version LIMIT 1")
            version = cursor.fetchone()
        except (Exception, psycopg2.DatabaseError) as e:
            cursor.close()
            conn.close()
            logger.error(f"Error al ejecutar la consulta: {e}")
            raise e
        else:
            cursor.close()
            conn.close()
            return version[0] if version else None

    def get_alembic_version_files_id(self):
        path_alembic = Path(self.app_path).parent / "alembic" / "versions"
        if not any(path_alembic.iterdir()):
            return []
        alembic_version_files = [file.name.split("_")[0] for file in path_alembic.iterdir()]
        return alembic_version_files

    def version_alembic_in_files(self, version):
        if not version and self.alembic_version_files:
            return True
        if version in self.alembic_version_files:
            return True
        return False

    def validate_changes_in_revision(self, name):
        alembic_files = self.get_alembic_version_files_id()
        file_id = list(set(alembic_files) - set(self.alembic_version_files))[0]
        file_path = Path(__file__).parent / "alembic" / "versions" / f"{file_id}_{name}.py"

        with open(file_path, "r") as file:
            file_content = file.read()

        tree = ast.parse(file_content)
        methods_with_pass = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in ["upgrade", "downgrade"]:
                if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                    methods_with_pass += 1

        if methods_with_pass == 2:
            try:
                file_path.unlink()
                return False
            except FileNotFoundError:
                print("El archivo no se encontró y no pudo ser eliminado.")
            except Exception as e:
                print(f"Ocurrió un error al intentar eliminar el archivo: {e}")

        return True

    def validate(self):
        logger.info("Start validate")
        validations = []
        for tenant in self.tenants or []:
            logger.info(f"Migrate tenant: {tenant}")
            host, port, user, password, name = self.get_postgres_config(Config.SERVICE_ID, tenant)
            alembic_version = self.get_alembic_version(host, port, user, password, name)
            validations.append(self.version_alembic_in_files(alembic_version))
        return all(validations)

    def revision(self):
        logger.info("Start revision")
        logger.info(f"Revision database saas-ms-sale-alembic")
        host, port, user, password, name = self.get_postgres_config(Config.SERVICE_ID, self.tenants[0])
        name = "saas-ms-sale-alembic"
        sql_connect = f"postgresql://{user}:{password}@{host}:{port}/{name}"
        os.environ["TENANT_URL"] = sql_connect
        name_file = f"automatic_revision_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"

        subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", name_file])
        return self.validate_changes_in_revision(name_file)

    def migrate(self):
        logger.info("Start migrations")
        for tenant in self.tenants or []:
            logger.info(f"Migrate tenant: {tenant}")
            host, port, user, password, name = self.get_postgres_config(Config.SERVICE_ID, tenant)
            sql_connect = f"postgresql://{user}:{password}@{host}:{port}/{name}"
            os.environ["TENANT_URL"] = sql_connect
            subprocess.run(["alembic", "upgrade", "head"])

    def push(self):
        pass
