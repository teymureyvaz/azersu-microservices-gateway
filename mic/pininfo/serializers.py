from rest_framework import serializers


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
