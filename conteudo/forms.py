from django import forms

from conteudo.models import Video, Categoria


class VideoForm(forms.ModelForm):
    error_messages = {
        'campo invalido' : "Campo inválido"
    }

    class Meta:
        model = Video
        fields = ('video_id','categoria', 'nome', 'url', 'capa', 'visualizacao', 'nota', 'sinopse')

    video_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    categoria = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório', },
        queryset=Categoria.objects.all().order_by(id),
        empty_label='--- Selecionar a Categoria ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True
    )

    nome = forms.CharField(
        error_messages = {'required', 'Campo obrigatório',},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True
    )

