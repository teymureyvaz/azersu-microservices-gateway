def subscriber_query(abonent_kodu,sozlesme_no,cur):
    v_return = cur.var(int)
    i_abonent_kodu = abonent_kodu
    i_sozlesme_no = sozlesme_no
    o_abonent_kodu = cur.var(str)
    o_sozlesme_no = cur.var(int)
    v_return = cur.var(str)
    o_adi = cur.var(str)
    o_soyadi = cur.var(str)
    o_baba_adi = cur.var(str)
    o_muessese_adi = cur.var(str)
    o_adres = cur.var(str)
    o_bakiye = cur.var(float)
    o_birim_fiyat = cur.var(float)
    o_nefer_sayisi = cur.var(int)
    o_sv_pin = cur.var(str)
    o_telefon_no = cur.var(str)
    o_e_posta_adresi = cur.var(str)
    o_son_odeme_tarihi = cur.var(str)
    o_son_odeme_tutari = cur.var(int)
    o_imtiyaz_tarihi = cur.var(str)
    o_imtiyaz_adedi = cur.var(str)
    o_kapama_tarihi = cur.var(str)
    o_kapama_sebebi = cur.var(str)
    o_sayac = cur.var(str)
    o_hizmet_turu = cur.var(str)
    o_sube_kodu = cur.var(str)
    o_illik_kullanim_tutar = cur.var(str)
    o_illik_odeme_tutar = cur.var(str)
    o_sonay_imtiyaz_tutar = cur.var(str)
    o_sozlesme_tarihi = cur.var(str)
    res = cur.execute(""" declare
    						io_abone pk_web.t_abone_bilgi;
    						v_return number;
    					begin
    						io_abone.abonent_kodu := :i_abonent_kodu;
    						io_abone.sozlesme_no  := :i_sozlesme_no;
    						v_return :=  pk_web.get_abone_bilgisi(io_abone => io_abone);
    						:v_return := v_return;
    						:o_sozlesme_no := io_abone.sozlesme_no;
    						:o_abonent_kodu := TO_CHAR(io_abone.abonent_kodu);
    						:o_adi := TO_CHAR(io_abone.Adi);
    						:o_soyadi := TO_CHAR(io_abone.Soyadi);
    						:o_baba_adi := TO_CHAR(io_abone.baba_adi);
    						:o_muessese_adi := TO_CHAR(io_abone.muessese_adi);
    						:o_adres := TO_CHAR(io_abone.Adres);
    						:o_bakiye := io_abone.Bakiye;
    						:o_birim_fiyat := io_abone.birim_fiyat;
    						:o_nefer_sayisi := io_abone.nefer_sayisi;
    						:o_sv_pin := TO_CHAR(io_abone.sv_pin);
    						:o_telefon_no := TO_CHAR(io_abone.telefon_no);
    						:o_e_posta_adresi := TO_CHAR(io_abone.e_posta_adresi);
    						:o_son_odeme_tarihi := TO_CHAR(io_abone.son_odeme_tarihi);
    						:o_son_odeme_tutari := io_abone.son_odeme_tutari;
    						:o_imtiyaz_tarihi := TO_CHAR(io_abone.imtiyaz_tarihi);
    						:o_imtiyaz_adedi := TO_CHAR(io_abone.imtiyaz_adedi);
    						:o_kapama_tarihi := TO_CHAR(io_abone.kapama_tarihi);
    						:o_kapama_sebebi := TO_CHAR(io_abone.kapama_sebebi);
    						:o_sayac := TO_CHAR(io_abone.sayacli_mi);
    						:o_hizmet_turu := TO_CHAR(io_abone.hizmet_turu);
    						:o_sube_kodu := io_abone.sube_kodu;
    						:o_illik_kullanim_tutar := io_abone.illik_kullanim_tutar;
    						:o_illik_odeme_tutar := io_abone.illik_odeme_tutar;
    						:o_sonay_imtiyaz_tutar := TO_CHAR(io_abone.sonay_imtiyaz_tutar);
    						:o_sozlesme_tarihi := TO_CHAR(io_abone.sozlesme_tarihi);
    					    end; """, i_abonent_kodu=i_abonent_kodu, i_sozlesme_no=i_sozlesme_no, v_return=v_return,
                      o_sozlesme_no=o_sozlesme_no,
                      o_abonent_kodu=o_abonent_kodu, o_adi=o_adi, o_soyadi=o_soyadi, o_baba_adi=o_baba_adi,
                      o_muessese_adi=o_muessese_adi, o_adres=o_adres,
                      o_bakiye=o_bakiye, o_birim_fiyat=o_birim_fiyat, o_nefer_sayisi=o_nefer_sayisi,
                      o_sv_pin=o_sv_pin, o_telefon_no=o_telefon_no,
                      o_e_posta_adresi=o_e_posta_adresi, o_son_odeme_tarihi=o_son_odeme_tarihi,
                      o_son_odeme_tutari=o_son_odeme_tutari, o_imtiyaz_tarihi=o_imtiyaz_tarihi,
                      o_imtiyaz_adedi=o_imtiyaz_adedi, o_kapama_tarihi=o_kapama_tarihi,
                      o_kapama_sebebi=o_kapama_sebebi, o_sayac=o_sayac, o_hizmet_turu=o_hizmet_turu,
                      o_sube_kodu=o_sube_kodu, o_illik_kullanim_tutar=o_illik_kullanim_tutar,
                      o_illik_odeme_tutar=o_illik_odeme_tutar, o_sonay_imtiyaz_tutar=o_sonay_imtiyaz_tutar,
                      o_sozlesme_tarihi=o_sozlesme_tarihi)
    # məlumatların gəlmədiyi halda xəta qaytarılır
    if abonent_kodu:
        if o_sozlesme_no == None:
            return {"status": 404, "message": "Not Found"}
    elif sozlesme_no:
        if o_abonent_kodu == None:
            return {"status": 404, "message": "Not Found"}

    return {
        "o_abonent_kodu":  o_abonent_kodu,
        "o_sozlesme_no" : o_sozlesme_no,
        "o_adi" :o_adi,
        "o_soyadi":o_soyadi,
        "o_baba_adi":o_baba_adi,
        "o_muessese_adi":o_muessese_adi,
        "o_adres":o_adres,
        "o_bakiye" :o_bakiye,
        "o_birim_fiyat":o_birim_fiyat,
        "o_nefer_sayisi":o_nefer_sayisi,
        "o_sv_pin":o_sv_pin,
        "o_telefon_no":o_telefon_no,
        "o_e_posta_adresi":o_e_posta_adresi,
        "o_son_odeme_tarihi":o_son_odeme_tarihi,
        "o_son_odeme_tutari":o_son_odeme_tutari,
        "o_imtiyaz_tarihi":o_imtiyaz_tarihi,
        "o_kapama_tarihi":o_kapama_tarihi,
        "o_kapama_sebebi":o_kapama_sebebi,
        "o_imtiyaz_adedi":o_imtiyaz_adedi,
        "o_sayac":o_sayac,
        "o_hizmet_turu":o_hizmet_turu,
        "o_sube_kodu":o_sube_kodu,
        "o_illik_kullanim_tutar":o_illik_kullanim_tutar,
        "o_illik_odeme_tutar":o_illik_odeme_tutar,
        "o_sonay_imtiyaz_tutar":o_sonay_imtiyaz_tutar,
        "o_sozlesme_tarihi":o_sozlesme_tarihi
    }
