from django.contrib import messages
from django.shortcuts import redirect, render
from utils.tools import string_capitalize

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter


def subscribe(request):
    """Renders the template corresponding to the newsletter user subscription form.

    (pt-BR) Renderiza o template correspondente ao formulário de inscrição
    do usuário na newsletter.

    Args:
        request (class): django.core.handlers.wsgi.WSGIRequest

    Returns:
        class: django.http.response.HttpResponse
    """

    form = NewsletterForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


def validate_subscribe(request):
    """Validates the user's subscription information for the newsletter.

    (pt_BR) Realiza a validação das informações de inscrição do usuário na
    newsletter.

    Args:
        request (class): django.core.handlers.wsgi.WSGIRequest

    Returns:
        class: django.http.response.HttpResponseRedirect
    """

    if request.method == 'POST':
        name = string_capitalize((request.POST.get('name')).strip())
        email = str(request.POST.get('email')).strip()

        if name and email:
            is_duplicated = True if len(Newsletter.objects.filter(
                email=email)) > 0 else False

            if not is_duplicated:
                try:
                    # Possible to refactor the code using the full_clean
                    # method to raise exceptions.
                    Newsletter(name=name, email=email).save()
                    level = messages.SUCCESS
                    message = 'E-mail cadastrado com sucesso! Obrigado por assinar \
                        nossa newsletter!'
                except Exception:
                    level = messages.ERROR
                    message = 'Erro inesperado ao realizar inscrição!'
            else:
                level = messages.INFO
                message = 'Muito obrigado pelo interesse! Seu email já está cadastrado \
                    para recebimento de nossa newsletter!'
        else:
            level = messages.WARNING
            message = 'Para assinar nossa newsletter, por favor forneça seu nome e \
                um endereço de email válido!'

        messages.add_message(request, level, message)

    return redirect('/newsletter')
