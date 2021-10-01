from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=255)
    expire_date = serializers.DateTimeField()
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=255)

class ResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=50)

class ResponseCheckSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=50)

class pinSerializer(serializers.Serializer):
    ad = serializers.CharField(max_length=64)
    soyad = serializers.CharField(max_length=64)
    ata_adi = serializers.CharField(max_length=64)
    dogum_tarixi = serializers.CharField(max_length=32)
    adres = serializers.DictField()
    vetendasliq = serializers.CharField(max_length=48)
    status = serializers.CharField(max_length=16)
    cins = serializers.CharField(max_length=16)
    foto = serializers.CharField(max_length=15000)
    bitme_tarixi = serializers.CharField(max_length=32)

class EmployeesSerializer(serializers.Serializer):
    contract_date = serializers.DateTimeField()
    department_name_id = serializers.CharField(max_length=32)
    employee_id = serializers.CharField(max_length=64)
    patronymic_name = serializers.CharField(max_length=64)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    org_unit_id = serializers.CharField(max_length=64)
    position_id = serializers.CharField(max_length=64)
    resign_date = serializers.DateTimeField()
    fin_code = serializers.CharField(max_length=32)
    rank = serializers.CharField(max_length=32)

class EmployeesParentSerializer(serializers.Serializer):
	employees = EmployeesSerializer(many=True)

class EmployeeSerializer(serializers.Serializer):
    contract_date = serializers.DateTimeField()
    department_name_id = serializers.CharField(max_length=32)
    employee_id = serializers.CharField(max_length=64)
    patronymic_name = serializers.CharField(max_length=64)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    org_unit_id = serializers.CharField(max_length=64)
    position_id = serializers.CharField(max_length=64)
    resign_date = serializers.DateTimeField()
    status = serializers.CharField(max_length=16)
    fin_code = serializers.CharField(max_length=32)
    rank = serializers.CharField(max_length=32)


class DepartmentNamesSerializer(serializers.Serializer):
    department_name_id = serializers.CharField(max_length=32)
    department_name = serializers.CharField(max_length=500)

class DepartmentNamesParentSerializer(serializers.Serializer):
	department_info = DepartmentNamesSerializer(many=True)

class DepartmentNameSerializer(serializers.Serializer):
    department_name_id = serializers.CharField(max_length=32)
    department_name = serializers.CharField(max_length=500)


class OrganisationNamesSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    org_name = serializers.CharField(max_length=500)

class OrganisationNamesParentSerializer(serializers.Serializer):
	organizations = OrganisationNamesSerializer(many=True)

class OrganisationNameSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    org_name = serializers.CharField(max_length=500)


class PositionNamesSerializer(serializers.Serializer):
    position_id = serializers.CharField(max_length=64)
    position_name = serializers.CharField(max_length=500)

class PositionNamesParentSerializer(serializers.Serializer):
	positions = PositionNamesSerializer(many=True)

class PositionNameSerializer(serializers.Serializer):
    position_id = serializers.CharField(max_length=64)
    position_name = serializers.CharField(max_length=500)


class DepartmentStructuresSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    parent_department_name_id = serializers.CharField(max_length=64)
    department_name_id = serializers.CharField(max_length=64)

class DepartmentStructuresParentSerializer(serializers.Serializer):
	department_structure = DepartmentStructuresSerializer(many=True)

class DepartmentStructureSerializer(serializers.Serializer):
    org_name_id = serializers.IntegerField()
    parent_department_name_id = serializers.CharField(max_length=64)
    department_name_id = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=16)

class SubscriberSerializer(serializers.Serializer):
    abonent_kodu = serializers.CharField(max_length=14)
    sozlesme_no = serializers.IntegerField()
    adi = serializers.CharField(max_length=20)
    soyadi = serializers.CharField(max_length=20)
    ata_adi = serializers.CharField(max_length=20)
    muessise_adi = serializers.CharField(max_length=50)
    adres = serializers.CharField(max_length=500)
    hesab = serializers.FloatField()
    kub_qiymeti = serializers.FloatField()
    nefer_sayi = serializers.IntegerField()
    s_v_pin = serializers.CharField(max_length=10)
    telefon_no = serializers.CharField(max_length=20)
    e_mail = serializers.CharField(max_length=20)
    son_odeme_tarixi = serializers.CharField(max_length=20)
    son_odeme_tutar = serializers.IntegerField()
    imtiyaz_tarixi = serializers.CharField(max_length=20)
    imtiyaz_ededi = serializers.CharField(max_length=20)
    baglanma_tarixi = serializers.CharField(max_length=20)
    baglanma_sebebi = serializers.CharField(max_length=100)
    saygac = serializers.CharField(max_length=30)
    xidmet_novu = serializers.CharField(max_length=100)
    sobe_kodu = serializers.IntegerField()
    illik_istifade_tutum = serializers.FloatField()
    illik_odeme_tutum = serializers.FloatField()
    son_ay_imtiyaz_tutum = serializers.CharField(max_length=20)
    sozlesme_tarixi = serializers.CharField(max_length=20)

class SubscriberSalesSerializer(serializers.Serializer):
    date = serializers.CharField()
    sale = serializers.FloatField()
    payment = serializers.FloatField()

class AdDeyismeSerializer(serializers.Serializer):
    abonent_kodu = serializers.CharField(max_length=15)
    muqavile_no = serializers.IntegerField()
    adi = serializers.CharField(max_length=30)
    soyadi =  serializers.CharField(max_length=30)
    ata_adi = serializers.CharField(max_length=30)
    ad_deyisme_tarixi = serializers.CharField(max_length=20)

class CounterInfoSerializer(serializers.Serializer):
    abonent_kodu = serializers.CharField(max_length=15)
    sozlesme_no = serializers.IntegerField()
    saygac_id = serializers.IntegerField()
    qurasdirilma_tarixi = serializers.CharField(max_length=15)
    saygac_no = serializers.IntegerField()