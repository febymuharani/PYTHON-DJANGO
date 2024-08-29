# SEMUA CODINGAN SEBELUM BASED VIEWS

#def delete(request,delete_id):
#    Instagram.objects.filter(id=delete_id).delete()
#    return redirect('sosmed:list')

# def list(request):
#    semua_akun = Instagram.objects.all()

#    context = {
#        'page_title' : 'Social Media',
#        'semua_akun' : semua_akun 
#    }
     
#    return render(request, 'sosmed/list.html', context)

#def update(request,update_id):
#    akun_update = Instagram.objects.get(id=update_id)


#    data = {
#        'nama_depan'      : akun_update.nama_depan,
#        'nama_belakang'   : akun_update.nama_belakang,
#        'username'        : akun_update.username,
#        'content'        : akun_update.content
#    }
#    akun_form = InstagramForm(request.POST or None,  initial=data, instance=akun_update)

#    if request.method == 'POST':
#        if akun_form.is_valid():
#            akun_form.save()


#        return redirect('sosmed:list')
    
#    context = {
#        'page_title' : 'Update Akun Instagram Mu',
#        'akun_form' : akun_form,
#    }

#    return render(request, 'sosmed/create.html', context)




#def create(request):
#    akun_form = InstagramForm(request.POST or None)

    
#    if request.method == 'POST':
#        if akun_form.is_valid():
#            akun_form.save()


#        return redirect('sosmed:list')
    
#    context = {
#        'page_title' : 'Tambah Akun Instagram Mu',
#        'akun_form' : akun_form,
#    }

#    return render(request, 'sosmed/create.html', context)
