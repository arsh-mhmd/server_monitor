from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index,name='index'),
    path('server_details/',views.server_details, name = 'server_details'),
    path('cpu_details/',views.cpu_details, name = 'cpu_details'),
    path('ram_details/',views.ram_details, name = 'ram_details'),
    path('disk_details/',views.disk_details, name = 'disk_details'),
    path('network_details/',views.network_details, name = 'network_details'),
    path("processes/", views.processes, name="processes"),
    path("HPC_benchmark/", views.HPC_benchmark, name="HPC_benchmark"),
    #path('line/',views.cpu_graph,name = 'line'),
    #path('gpu_temp_graph/',views.gpu_temp_graph,name = 'gpu_temp_graph'),
    #path('cpu_temp_graph/',views.cpu_temp_graph,name = 'cpu_temp_graph'),
    #path('gpu_load/',views.gpu_load_graph,name = 'gpu_load'),
    #path('percent/',views.disk_graph,name = 'percent'),
    #path('memory_info/',views.memory_info,name = 'memory_info'),
]

#urlpatterns = [
#    path("", views.index, name="dashboard"),
#    path("charts/", views.charts, name="charts"),
#    path("widgets/", views.widgets, name="widgets"),
#    path("tables/", views.tables, name="tables"),
#    path("grid/", views.grid, name="grid"),
#    path("form-basic/", views.form_basic, name="form-basic"),
#    path("form-wizard/", views.form_wizard, name="form-wizard"),
#    path("buttons/", views.buttons, name="buttons"),
#    path("icon-material/", views.icon_material, name="icon-material"),
#    path("icon-fontawesome/", views.icon_fontawesome, name="icon-fontawesome"),
#    path("elements/", views.elements, name="elements"),
#    path("gallery/", views.gallery, name="gallery"),
#    path("invoice/", views.invoice, name="invoice"),
#    path("chat/", views.chat, name="chat"),
#]