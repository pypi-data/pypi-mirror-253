from django.db import models

from isapilib.core.models import BaseModel
from isapilib.utilities import execute_query


class Venta(BaseModel):
    id = models.AutoField(db_column='ID', primary_key=True)
    mov = models.CharField(db_column='Mov', default='Cita Servicio', max_length=20)
    mov_id = models.CharField(db_column='MovID', max_length=20, null=True, blank=True)
    fecha_requerida = models.DateTimeField(db_column='FechaRequerida')
    hora_requerida = models.CharField(db_column='HoraRequerida', max_length=5)
    servicio_modelo = models.CharField(db_column='ServicioModelo', max_length=4)
    servicio_placas = models.CharField(db_column='ServicioPlacas', max_length=20)
    servicio_serie = models.CharField(db_column='ServicioSerie', max_length=50)
    servicio_articulo = models.CharField(db_column='ServicioArticulo', max_length=20)
    empresa = models.CharField(db_column='Empresa', max_length=5)
    moneda = models.CharField(db_column='Moneda', default='Pesos', max_length=10)
    cliente = models.CharField(db_column='Cliente', max_length=10)
    sucursal = models.IntegerField(db_column='Sucursal')
    almacen = models.CharField(db_column='Almacen', max_length=10)
    uen = models.IntegerField(db_column='UEN')
    concepto = models.CharField(db_column='Concepto', default='Publico', max_length=50)
    usuario = models.CharField(db_column='Usuario', default='SOPDESA', max_length=10)
    estatus = models.CharField(db_column='Estatus', default='SINAFECTAR', max_length=15)
    tipo_cambio = models.FloatField(db_column='TipoCambio', default=1)
    referencia = models.CharField(db_column='Referencia', max_length=50)
    comentarios = models.TextField(db_column='Comentarios')
    agente = models.CharField(db_column='Agente', max_length=10)
    origen_id = models.CharField(db_column='OrigenID', max_length=20)
    fecha_emision = models.DateTimeField(db_column='FechaEmision')
    observaciones = models.CharField(db_column='Observaciones', max_length=100)
    fecha_entrega = models.DateTimeField(db_column='FechaEntrega')
    servicio_kms = models.IntegerField(db_column='ServicioKms')

    class Meta:
        db_table = 'Venta'
        managed = False

    def afectar(self, **kwargs):
        db_name = kwargs.get('using', 'default')

        params = dict(
            ID=self.id,
            Modulo=kwargs.get('modulo', 'VTAS'),
            Accion=kwargs.get('accion', 'AFECTAR'),
            Base=kwargs.get('base', 'Todo'),
            GenerarMov=kwargs.get('generarmov', False),
            Usuario=kwargs.get('usuario', 'SOPDESA'),
            SincroFinal=kwargs.get('sincrofinal', False),
            EnSilencio=kwargs.get('ensilencio', 1),
            FechaRegistro=kwargs.get('fecharegistro', False),
            Conexion=kwargs.get('conexion', False),
            Estacion=kwargs.get('estacion', 1000),
            FueraLinea=kwargs.get('fueralinea', False)
        )
        params = {key: value for key, value in params.items() if value}

        query = f'''
            SET NOCOUNT ON;
            DECLARE @Ok VARCHAR(MAX), @OkRef VARCHAR(MAX);
            EXEC spAfectar {','.join([f'@{i}=%s' for i in params.keys()])}, @Ok=@Ok OUTPUT, @OkRef=@OkRef OUTPUT;
            SELECT @Ok, @OkRef;
            '''

        cursor = execute_query(query, sp_params=list(params.values()), using=db_name)
        ok, ok_ref = cursor[0]
        if ok is not None or ok_ref is not None:
            return [False, ok_ref]

        self.refresh_from_db()
        return [True, '']


class Vin(BaseModel):
    vin = models.CharField(db_column='VIN', max_length=20, primary_key=True)
    articulo = models.CharField(db_column='Articulo', max_length=20)
    modelo = models.CharField(db_column='Modelo', max_length=4)
    placas = models.CharField(db_column='Placas', max_length=20)
    cliente = models.CharField(db_column='Cliente', max_length=10)
    comentarios_primera_llamada = models.CharField(db_column='ComentariosPrimeraLLamada', max_length=1000)
    color_exterior = models.CharField(db_column='ColorExterior', max_length=10)
    motor = models.CharField(db_column='Motor', max_length=20)
    garantia_vencimiento = models.DateTimeField(db_column='GarantiaVencimiento')
    empresa = models.CharField(db_column='Empresa', max_length=5)

    class Meta:
        db_table = 'VIN'
        managed = False


class Cte(BaseModel):
    cliente = models.CharField(db_column='Cliente', max_length=10, primary_key=True)
    email = models.CharField(db_column='eMail1', max_length=50)
    estatus = models.CharField(db_column='Estatus', max_length=15, default='ALTA')
    colonia = models.CharField(db_column='Colonia', max_length=100, default='')
    rfc = models.CharField(db_column='RFC', max_length=20)
    personal_nombres = models.CharField(db_column='PersonalNombres', max_length=80)
    personal_apellido_paterno = models.CharField(db_column='PersonalApellidoPaterno', max_length=50)
    personal_apellido_materno = models.CharField(db_column='PersonalApellidoMaterno', max_length=50)
    telefonos = models.CharField(db_column='Telefonos', max_length=30)
    direccion = models.CharField(db_column='Direccion', max_length=100)
    codigo_postal = models.CharField(db_column='CodigoPostal', max_length=100)
    poblacion = models.CharField(db_column='Poblacion', max_length=100)
    pais = models.CharField(db_column='Pais', max_length=150)
    estado = models.CharField(db_column='Estado', max_length=40)
    personal_telefono_movil = models.CharField(db_column='PersonalTelefonoMovil', max_length=30)
    fiscal_regimen = models.CharField(db_column='FiscalRegimen', max_length=30)
    contactar = models.CharField(db_column='Contactar', max_length=30, default='0')
    fecha_nacimiento = models.DateTimeField(db_column='FechaNacimiento')
    direccion_numero = models.CharField(db_column='DireccionNumero', max_length=20)
    nombre = models.CharField(db_column='Nombre', max_length=254)

    class Meta:
        db_table = 'Cte'
        managed = False


class Empresa(BaseModel):
    empresa = models.CharField(db_column='Empresa', max_length=5, primary_key=True)

    class Meta:
        db_table = 'Empresa'
        managed = False


class Agente(BaseModel):
    agente = models.CharField(db_column='Agente', max_length=10, primary_key=True)

    class Meta:
        db_table = 'Agente'
        managed = False


class Art(BaseModel):
    articulo = models.CharField(db_column='Articulo', max_length=20, primary_key=True)

    class Meta:
        db_table = 'Art'
        managed = False
