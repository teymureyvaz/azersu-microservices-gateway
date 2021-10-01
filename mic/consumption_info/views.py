from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
import json
from . import serializers
import os
from .helper import connect_ode, connect_web,getLastMonths,myfloat
import cx_Oracle as oracle
from datetime import *
from .queries import subscriber_query
class SubscriberView(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        unserializedobject = self.get_context_data(request)

        # 'status' key-i  obyektdə olduqu zaman deməli obyekt xəta obyektidir,ResponseSerializer obyekti ilə qaytarılır.
        if 'status' in unserializedobject:
            serializer = serializers.ResponseSerializer(instance=unserializedobject)
        else:
            serializer = serializers.SubscriberSerializer(instance=unserializedobject)

        return Response(serializer.data)

    def get_context_data(self, request):
        con = connect_ode()

        # Verilənlər bazası ilə əlaqə qurulmadıqda xəta verilir
        if con == None:
            return {"status": 500, "message": "Internal Server Error"}
        cur = con.cursor()
        subscriber_data = None
        abonent_kodu = None
        sozlesme_no = None

        # Göndərilən JSON obyektinin düzgün olub olmaması yoxlanılır,əgər düzgün deyilsə xəta qaytarılır
        try:
            subscriber_data = json.loads(request.body)
        except ValueError as error:
            return {"status":400,"message":"Bad Request"}
            print("invalid json: %s" % error)

        # Daxil olunan JSON obyektində 1 açar sözdən çox key olduqda xəta kodu qaytarılır
        if len(subscriber_data) > 1:
            return {"status": 400, "message": "Bad Request"}

        # Sözləşmə nömrəsi yaxud Abonent kodu dəyərlərindən birinin JSON obyektində olub olmadıqı yoxlanılır
        if 'sozlesme_no' in subscriber_data:
            sozlesme_no = subscriber_data['sozlesme_no']
            # Sözləşmə nömrəsi string olquda xəta kodu qaytarılır
            if isinstance(sozlesme_no,str):
                return {"status":400,"message":"Bad Request"}
            print(sozlesme_no)
        elif 'abonent_kodu' in subscriber_data:
            abonent_kodu = subscriber_data['abonent_kodu']
            print(abonent_kodu)
            print(type(abonent_kodu))
            if isinstance(abonent_kodu, int):
                # Abonent kodu int olquda xəta kodu qaytarılır
                return {"status":400,"message":"Bad Request"}

            # Abonent kodunun daxilində rəqəmdən başqa hərf yaxud digər simvol olduqda həmçinin
            # abonent kodunun uzunluqu 13 yaxud 6-dan fərqləndiyi hald xəta qaytarılır
            if len(abonent_kodu) == 13 or len(abonent_kodu) == 6:
                if abonent_kodu.isdigit():
                    pass
                else:
                    return {"status":400,"message":"Bad Request"}
            else:
                return {"status":400,"message":"Bad Request"}
        else:
            return {"status": 400, "message": "Bad Request"}

        result = subscriber_query(abonent_kodu,sozlesme_no,cur)
        
        if 'status' in result:
            return result
        else:
            return {'abonent_kodu': result['o_abonent_kodu'].getvalue(),
                'sozlesme_no': result['o_sozlesme_no'].getvalue(),
                'adi': result['o_adi'].getvalue(),
                'soyadi': result['o_soyadi'].getvalue(),
                'ata_adi': result['o_baba_adi'].getvalue(),
                'muessise_adi': result['o_muessese_adi'].getvalue(),
                'adres': result['o_adres'].getvalue(),
                'hesab': result['o_bakiye'].getvalue(),
                'kub_qiymeti': result['o_birim_fiyat'].getvalue(),
                'nefer_sayi': result['o_nefer_sayisi'].getvalue(),
                's_v_pin': result['o_sv_pin'].getvalue(),
                'telefon_no': result['o_telefon_no'].getvalue(),
                'e_mail': result['o_e_posta_adresi'].getvalue(),
                'son_odeme_tarixi': result['o_son_odeme_tarihi'].getvalue(),
                'son_odeme_tutar': result['o_son_odeme_tutari'].getvalue(),
                'imtiyaz_tarixi': result['o_imtiyaz_tarihi'].getvalue(),
                'imtiyaz_ededi': result['o_imtiyaz_adedi'].getvalue(),
                'baglanma_tarixi': result['o_kapama_tarihi'].getvalue(),
                'baglanma_sebebi': result['o_kapama_sebebi'].getvalue(),
                'saygac': result['o_sayac'].getvalue(),
                'xidmet_novu': result['o_hizmet_turu'].getvalue(),
                'sobe_kodu': result['o_sube_kodu'].getvalue(),
                'illik_istifade_tutum': result['o_illik_kullanim_tutar'].getvalue(),
                'illik_odeme_tutum': result['o_illik_odeme_tutar'].getvalue(),
                'son_ay_imtiyaz_tutum': result['o_sonay_imtiyaz_tutar'].getvalue(),
                'sozlesme_tarixi': result['o_sozlesme_tarihi'].getvalue()
                }

class SubscriberSalesView(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request,month):
        unserializedobject = self.get_context_data(request,month)
        # 'status' key-i obyektdə olduqu zaman deməli obyekt xəta obyektidir,cavab ResponseSerializer obyekti ilə qaytarılır.
        if 'status' in unserializedobject:
            serializer = serializers.ResponseSerializer(instance=unserializedobject)
        else:
            serializer = serializers.SubscriberSalesSerializer(instance=unserializedobject,many=True)

        return Response(serializer.data)

    def get_context_data(self, request,month):
        # ay dəyəri sıfra bərabər olduqu halda xəta qaytarılır
        if month==0:
            return {"status":400,"message":"Bad Request"}
        subscriber_data = None

        # Göndərilən JSON obyektinin düzgün olub olmaması yoxlanılır,əgər düzgün deyilsə xəta qaytarılır
        try:
            subscriber_data = json.loads(request.body)
        except ValueError as error:
            return {"status":400,"message":"Bad Request"}
            print("invalid json: %s" % error)

        # Göndərilən JSON obyektinində  "abonent_kodu" key-i  olmadıqda xəta qaytarılır
        try:
            abonent_kodu = subscriber_data['abonent_kodu']
        except:
            return {"status": 400, "message": "Bad Request"}

        # Göndərilən JSON obyektinində 1-dən çox key olduqu halda xəta qaytarılır
        if len(subscriber_data) > 1:
            return {"status": 400, "message": "Bad Request"}
        # Abonent kodunun uzunluqu 13 yaxud 6-dan fərqləndiyi halda xəta qaytarılır
        if len(abonent_kodu) == 13 or len(abonent_kodu) == 6:
            pass
        else:
            return {"status": 400, "message": "Bad Request"}

        con = connect_ode()
        # Verilən bazası ilə əlaqə qurulmadıqı halda xəta qaytarılır
        if con == None:
            return {"status": 500, "message": "Internal Server Error"}
        cur = con.cursor()
        l_string = cur.var(str)
        v_return = cur.var(int)
        res = cur.execute("""
                     declare
                        i_abonent_kodu varchar2(200);
                        io_abone pk_web.t_abone_satis_odenis_tab;
                        v_return number;
                        l_string varchar2(30000);
                    begin
                        i_abonent_kodu := :i_abonent_kodu;
                        io_abone.delete;
                        v_return := pk_web.get_abone_satis_odenis(i_sozlesme_no=>null, i_abonent_kodu=>i_abonent_kodu, io_abone =>io_abone);
                        :v_return := v_return;
                        if v_return >= 0 then
                            for z in io_abone.first..io_abone.last
                            loop
                                l_string := l_string || (io_abone(z).dovr || '-' || io_abone(z).satis ||  '-' || io_abone(z).odenis || '|');
                            end loop;
                        end if;
                        :l_string := l_string;
                    end;

                """,i_abonent_kodu=abonent_kodu,l_string=l_string,v_return=v_return)
        # Satışlar l_string dəyişənindən götürülür
        subscriber_sales = l_string.getvalue()
        # Satış stringi parse olunur
        subscriber_sales = subscriber_sales.split("|")
        parsed_subscriber_sales = list()

        # satışlarda date, sale və payment dəyərləri ayrılır
        for item in subscriber_sales:
            parsed_subscriber_sales.append((item[0:4] + "-" + item[4:6],item[6:].split("-")))
        # listdən sonuncu dəyər silinir,çünki bu dəyər parse zamani artıq yaranır.
        del parsed_subscriber_sales[-1]
        # parse zamanı satış və ödəniş elementində əlavə dəyər yaranır,burada o silinir
        for item in parsed_subscriber_sales:
            del item[1][0]
        # parsed_subscriber_sales2 adlı dict yaradılır,bu dict-ə dəyərlər mənimsədilir.
        parsed_subscriber_sales2 = dict()
        for i,item in enumerate(parsed_subscriber_sales):
            parsed_subscriber_sales2[i] = {
                    "date": str(datetime.strptime(item[0], '%Y-%m'))[0:7],
                    "sale": myfloat(item[1][0]),
                    "payment": myfloat(item[1][1])
              }
        # last_months dəyişəninə istifadəçinin icazəsinə uyğun olaraq qaytarılacaq ay listi gətirilir.
        last_months = getLastMonths(month)
        last_results = []
        # last_months listində olan tarixlər ilə verilən bazasından gələn datalar müqayisə edilir,icazə verilən tarixlər ilə
        # bərabər tarix olduqu halda last_results listinə əlavə edilir.
        for key,value in parsed_subscriber_sales2.items():
            for date in last_months:
                if value['date'] == date:
                    last_results.append(value)
        return last_results

class AdDeyisiklik(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        unserializedobject = self.get_context_data(request)
        # 'status' key-i  obyektdə olduqu zaman deməli obyekt xəta obyektidir,cavab ResponseSerializer obyekti ilə qaytarılır.
        if 'status' in unserializedobject:
            serializer = serializers.ResponseSerializer(instance=unserializedobject)
        else:
            serializer = serializers.AdDeyismeSerializer(instance=unserializedobject,many=True)

        return Response(serializer.data)

    def get_context_data(self, request):
        subscriber_data = None
        # JSON obyektinin düzgün olub olmadıqı yoxlanılır,düzgun olmadıqı halda xəta qaytarılır
        try:
            subscriber_data = json.loads(request.body)
        except ValueError as error:
            return {"status":400,"message":"Bad Request"}
            print("invalid json: %s" % error)

        # JSON obyektində "abonent_kodu" key-inin olub olmadıqı yoxlanılır,olmadıqı halda xəta qaytarılır
        try:
            abonent_kodu = subscriber_data['abonent_kodu']
        except:
            return {"status": 400, "message": "Bad Request"}

        # JSON obyektində 1-dən çox key-in olduqu halda xəta qaytarılır
        if len(subscriber_data) > 1:
            return {"status": 400, "message": "Bad Request"}
        #Abonent kodunun uzunluqu 13 yaxud 6-dan fərqli olduqu halda xəta qaytarılır
        if len(abonent_kodu) == 13 or len(abonent_kodu) == 6:
            pass
        else:
            return {"status": 400, "message": "Bad Request"}
        con = connect_ode()
        # Verilən bazasına qoşulmaq mümkün olmadıqı halda xəta qaytarılır
        if con == None:
            return {"status": 500, "message": "Internal Server Error"}

        cur = con.cursor()
        cur.prepare('SELECT * FROM web.web_ad_deyisiklik_vw WHERE ABONENT_KODU = :abonent_kodu')
        cur.execute(None, {'abonent_kodu': abonent_kodu})
        res = cur.fetchall()
        # verilən bazasından qayıdan dəyərin uzunluqu 0-a bərabər olduqu halda xəta qaytaılır
        if len(res) == 0:
            return {"status": 404, "message": "Not Found"}
        result_dict = {}
        result_list = []
        # verilən bazasından gələn dəyərlər result_dict obyektinə əlavə edilir
        for i,item in enumerate(res):
            result_dict[i] =  {"abonent_kodu":item[0],
                "muqavile_no": item[1],
                "adi": item[2],
                "soyadi": item[3],
                "ata_adi" : item[4],
                "ad_deyisme_tarixi": item[5]
                }
        # result_dict obyektindəki yalnız value-lər yeni listə əlavə edilib qaytarılır
        for key,value in result_dict.items():
            result_list.append(value)

        return result_list


class CounterInfoView(views.APIView):
    def get(self, request):
        content = {'content': 'Method Not Allowed'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        unserializedobject = self.get_context_data(request)
        # 'status' key-i  obyektdə olduqu zaman deməli obyekt xəta obyektidir,cavab ResponseSerializer obyekti ilə qaytarılır.
        if 'status' in unserializedobject:
            serializer = serializers.ResponseSerializer(instance=unserializedobject)
        else:
            serializer = serializers.CounterInfoSerializer(instance=unserializedobject,many=True)

        return Response(serializer.data)

    def get_context_data(self, request):
        subscriber_data = None
        # JSON obyektinin düzgün olub olmadıqı yoxlanılır,düzgun olmadıqı halda xəta qaytarılır
        try:
            subscriber_data = json.loads(request.body)
        except ValueError as error:
            return {"status":400,"message":"Bad Request"}
            print("invalid json: %s" % error)

        # JSON obyektində "abonent_kodu" key-inin olub olmadıqı yoxlanılır,olmadıqı halda xəta qaytarılır
        try:
            abonent_kodu = subscriber_data['abonent_kodu']
        except:
            return {"status": 400, "message": "Bad Request"}

        if len(subscriber_data) > 1:
            return {"status": 400, "message": "Bad Request"}
        # Abonent kodunun uzunluqu 13 yaxud 6-dan fərqli olduqu halda xəta qaytarılır
        if len(abonent_kodu) == 13 or len(abonent_kodu) == 6:
            pass
        else:
            return {"status": 400, "message": "Bad Request"}
        con = connect_ode()
        cur = con.cursor()
        # Verilən bazasına qoşulmaq mümkün olmadıqı halda xəta qaytarılır
        if con == None:
            return {"status": 500, "message": "Internal Server Error"}

        cur.prepare('SELECT * FROM web.web_sayac_melumat_vw WHERE ABONENT_KODU = :abonent_kodu')
        cur.execute(None, {'abonent_kodu': abonent_kodu})
        res = cur.fetchall()
        # verilən bazasından qayıdan dəyərin uzunluqu 0-a bərabər olduqu halda xəta qaytaılır
        if len(res) == 0:
            return {"status": 404, "message": "Not Found"}
        result_dict = {}
        result_list = []
        # verilən bazasından gələn dəyərlər result_dict obyektinə əlavə edilir
        for i,item in enumerate(res):
            result_dict[i] =  {
                "abonent_kodu":item[0],
                "sozlesme_no": item[1],
                "saygac_id": item[2],
                "qurasdirilma_tarixi": item[3],
                "saygac_no" : item[4],
                }
        # result_dict obyektindəki yalnız value-lər yeni listə əlavə edilib qaytarılır
        for key,value in result_dict.items():
            result_list.append(value)

        return result_list