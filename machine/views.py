# Create your views here.

from .forms import PostForm

def post_new(request):
    form = PostForm()
    return render(request, 'machine/arquivo.html', {'form': form})
