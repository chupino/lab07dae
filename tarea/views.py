from django.shortcuts import redirect, render
from tarea.models import Evento, RegistroEvento, Usuario
from django.views.generic.edit import CreateView
from .forms import EventoForm,UserRegistrationForm, RegistroEventoForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

def eventos_list(request):
    selected_month = request.GET.get('mes')

    if selected_month:
        events = Evento.objects.filter(fecha__month=selected_month)
    else:
        events = Evento.objects.all()

    return render(request, 'lista_eventos.html', {'events': events})

def usuario_mas_participativo(request):
    usuario_mas_participativo = Usuario.objects.annotate(eventos_participados=Count('registroevento')).order_by('-eventos_participados').first()
    return render(request, 'user.html', {'usuario_mas_participativo': usuario_mas_participativo})
def eventos_realizados_por_usuario(request):
    usuarios = Usuario.objects.all()

    usuario_seleccionado = None
    eventos_realizados = []

    if 'usuario_id' in request.GET:
        usuario_id = request.GET['usuario_id']
        usuario_seleccionado = Usuario.objects.get(id=usuario_id)
        eventos_realizados = RegistroEvento.objects.filter(usuario=usuario_seleccionado)

    return render(request, 'eventos_realizados_por_usuario.html', {'usuarios': usuarios, 'usuario_seleccionado': usuario_seleccionado, 'eventos_realizados': eventos_realizados})
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('eventos_list') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def evento_detail(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    inscritos = evento.inscritos.all()
    return render(request, 'evento_detail.html', {'evento': evento, 'inscritos': inscritos})
def editar_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('eventos_list')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})
def eliminar_evento(request, evento_id):
    try:
        evento = Evento.objects.get(id=evento_id)
        evento.delete()
        return redirect('eventos_list')
    except Evento.DoesNotExist:
        return redirect('eventos_list')
def inscribir_persona_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            evento = form.cleaned_data['evento']
            RegistroEvento.objects.create(usuario=usuario, evento=evento)
            return redirect('eventos_list') 
    else:
        form = RegistroEventoForm()
    return render(request, 'inscripcion_evento.html', {'form': form})

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento_form.html'
    success_url = '/tarea/'

    def form_valid(self, form):
        return super().form_valid(form)