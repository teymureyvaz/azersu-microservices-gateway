from rest_framework import serializers

class SubscriberSerializer(serializers.Serializer):
    abonent_kodu = serializers.CharField(max_length=15)
    sozlesme_no = serializers.IntegerField()
    adi = serializers.CharField(max_length=50)
    soyadi = serializers.CharField(max_length=50)
    ata_adi = serializers.CharField(max_length=50)
    muessise_adi = serializers.CharField(max_length=100)
    adres = serializers.CharField(max_length=500)
    hesab = serializers.FloatField()
    kub_qiymeti = serializers.FloatField()
    nefer_sayi = serializers.IntegerField()
    s_v_pin = serializers.CharField(max_length=20)
    telefon_no = serializers.CharField(max_length=20)
    e_mail = serializers.CharField(max_length=50)
    son_odeme_tarixi = serializers.CharField(max_length=20)
    son_odeme_tutar = serializers.IntegerField()
    imtiyaz_tarixi = serializers.CharField(max_length=20)
    imtiyaz_ededi = serializers.CharField(max_length=20)
    baglanma_tarixi = serializers.CharField(max_length=20)
    baglanma_sebebi = serializers.CharField(max_length=200)
    saygac = serializers.CharField(max_length=30)
    xidmet_novu = serializers.CharField(max_length=100)
    sobe_kodu = serializers.IntegerField()
    illik_istifade_tutum = serializers.FloatField()
    illik_odeme_tutum = serializers.FloatField()
    son_ay_imtiyaz_tutum = serializers.IntegerField()
    sozlesme_tarixi = serializers.CharField(max_length=20)



class ResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=50)

class SubscriberSalesSerializer(serializers.Serializer):
    date = serializers.CharField(max_length=20)
    sale = serializers.FloatField()
    payment = serializers.FloatField()


class AdDeyismeSerializer(serializers.Serializer):
    abonent_kodu = serializers.CharField(max_length=15)
    muqavile_no = serializers.IntegerField()
    adi = serializers.CharField(max_length=50)
    soyadi =  serializers.CharField(max_length=50)
    ata_adi = serializers.CharField(max_length=50)
    ad_deyisme_tarixi = serializers.CharField(max_length=20)

class CounterInfoSerializer(serializers.Serializer):
    abonent_kodu = serializers.CharField(max_length=15)
    sozlesme_no = serializers.IntegerField()
    saygac_id = serializers.IntegerField()
    qurasdirilma_tarixi = serializers.CharField(max_length=20)
    saygac_no = serializers.IntegerField()