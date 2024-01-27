from django.apps import apps
from django.conf import settings
from django.db import connections


def execute_query(query, sp_params=None, using='default'):
    cursor = connections[using].cursor()

    try:
        print(query, sp_params or [])
        cursor.execute(query, sp_params or [])
        results = cursor.fetchall()
    finally:
        cursor.close()

    return results


def execute_sp(sp_name, sp_params=None, using='default'):
    sp_params = sp_params or []
    output_params = execute_query('''
        SELECT 
            PARAMETER_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
        FROM information_schema.parameters WHERE SPECIFIC_NAME = %s AND PARAMETER_MODE = 'INOUT'
        ''', [sp_name], using=using)

    sp_call = 'DECLARE'
    return execute_query(sp_call, sp_params, using)


def get_sucursal(filter, mov, using='default'):
    branch_model_path = apps.get_model(getattr(settings, 'BRANCH_MODEL', 'isapilib.SepaBranch'), require_ready=False)
    sucursal = branch_model_path.objects.get(**filter).id_intelisis
    results = execute_query("SELECT dbo.fnCA_GeneraSucursalValida('VTAS', %s, %s)", [mov, sucursal], using=using)
    return results[0][0]


def get_almacen(sucursal, mov, using='default'):
    results = execute_query("SELECT dbo.fnCA_GeneraAlmacenlValido('VTAS', %s, %s)", [mov, sucursal], using=using)
    return results[0][0]


def get_uen(sucursal, mov, using='default'):
    results = execute_query("SELECT dbo.fnCA_GeneraUENValida('VTAS', %s, %s, 'Publico')", [mov, sucursal], using=using)
    return results[0][0]


def get_param_sucursal(sucursal, key, using='default'):
    return execute_query('SELECT dbo.fnCA_CatParametrosSucursalValor(%s, %s)', [sucursal, key], using=using)[0][0]
