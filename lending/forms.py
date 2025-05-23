from django import forms
from django.forms import inlineformset_factory
from .models import Book, Request, User, BookCopy, AlternateCover
from .models import Profile
from .models import Collection
from .models import Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_title',
            'book_author',
            'book_genre',
            'isbn',
            'pub_year',
            'summary',
            'total_copies',
            'book_cover',
        ]
        widgets = {
            'pub_year': forms.NumberInput(attrs={'min': 1000, 'max': 9999}),
            'total_copies': forms.NumberInput(attrs={'min': 1}),
        }


    def clean_total_copies(self):
        value = self.cleaned_data.get('total_copies')
        if value is None or value < 1:
            raise forms.ValidationError("Total copies must be at least 1.")
        return value


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class CollectionForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    allowed_users = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(is_staff=False),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Collection
        fields = ['collection_name', 'private', 'description', 'books', 'allowed_users']
        
    def __init__(self, *args, user_is_staff=False, **kwargs):
        super().__init__(*args, **kwargs)
        if not user_is_staff:
            # Hide private field for non-staff users
            self.fields['private'].widget = forms.HiddenInput()
            self.fields['private'].initial = False

        edit_collection = kwargs.get('instance', None)
        public_books = Book.objects.exclude(collection__private=True)
        if edit_collection:
            my_books = edit_collection.books.all()
            self.fields['books'].queryset = (public_books | my_books).distinct()
        else:
            self.fields['books'].queryset = public_books.distinct()

class AddLibrarianForm(forms.Form):
    email = forms.EmailField(label='', help_text='Input Librarian Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=Review.RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'star-rating'}),
        required=True
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Write your review here...',
                'class': 'form-control'
            })
        }
        error_messages = {
            'rating': {
                'required': "Please select a rating.",
            },
            'comment': {
                'required': "Please write a comment.",
            },
        }

class BookCopyForm(forms.ModelForm):
    location = forms.ChoiceField(
        choices=BookCopy.LIBRARY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = BookCopy
        fields = ['location']

BookCopyFormSet = inlineformset_factory(
    Book, 
    BookCopy, 
    form=BookCopyForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True
)

class AlternateCoverForm(forms.ModelForm):
    class Meta:
        model = AlternateCover
        fields = ['image']

AlternateCoverFormset = inlineformset_factory(
    Book,
    AlternateCover,
    form=AlternateCoverForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True
)
