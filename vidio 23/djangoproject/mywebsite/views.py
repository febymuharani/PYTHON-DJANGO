from django.http import HttpResponse, Http404

def link(request, page):
    heading = "<h1> Page Teks </h1>"
    str = "<h1>{}</h1>".format(page)
    return HttpResponse(heading + str)


def index(request):
    return HttpResponse("<h1>HOME</h1>")



'''URLS UNTUK MENGAMBIL SELURUH ANGKA'''
'''path('<int:input>/', views.angka, name='angka')'''
def angka(request,input):

    heading = "<h1> Page Angka </h1>"
    result = heading + str(input)
    return HttpResponse(result)



'''URLS UNTUK MENGAMBIL ANGKA SESUAI YANG DI MINTA'''
'''path('<int:tahun>/<int:bulan>/<int:hari>/', views.tanggal, name='tanggal'),'''
#CARA SEDERHANA
def tanggal(request, tahun,bulan,hari):
    heading = "<h1> Page Tanggal </h1>"

    if not (1000 <= tahun <= 9999):
        raise Http404("Tahun harus 4 digit.")
    if not (1 <= bulan <= 12):
        raise Http404("Bulan tidak valid.")
    if not (1 <= hari <= 31):
        raise Http404("Hari tidak valid.")
    

    dataTanggal = "<h2>{}/{}/{}</h2>".format(tahun,bulan,hari)
    return HttpResponse(heading + dataTanggal)

# CARA PANJANG
#def tanggal(request, first_input,second_input,third_input):
#    heading = "<h1> Page Tanggal </h1>"
#    if 1000 <= first_input <= 9999 and 10 <= second_input <= 99:
#        result = heading + f"tahun: {first_input} <br> bulan: {second_input} <br> tanggal: {third_input}"
#        return HttpResponse(result)
#    else:
#        raise Http404("Input harus berupa 4 digit angka.")





    