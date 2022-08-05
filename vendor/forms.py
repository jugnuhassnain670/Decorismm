from django.forms import ModelForm
from product.models import Product,ProductImage
from blog.models import blogs
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields =['category','title','description','price','image']
        
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].widget.attrs.update({  
            'class':'form-select'
                    
        })
        self.fields['title'].widget.attrs.update({  
            'class':'form-control' 
            
                    
        })
        self.fields['description'].widget.attrs.update({  
            'class':'form-control'  
            
                    
        })
        self.fields['price'].widget.attrs.update({  
            'class':'form-control'
            
                    
        })
        self.fields['image'].widget.attrs.update({  
            'class':'form-control'
                    
        })

class ProductImageForm(ModelForm):
    class Meta:
        model =ProductImage
        fields=['image']
        
class BlogForm(ModelForm):
    class Meta:
        model= blogs
        fields =[
            'vendor',
            'title',
            'description',
            'image',
            'thumbnail'
        ]
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['vendor'].widget.attrs.update({  
            'class':'form-select'
                    
        })
        self.fields['title'].widget.attrs.update({  
            'class':'form-control',  
            
                    
        })
        self.fields['description'].widget.attrs.update({  
            'class':'form-control',  
            
                    
        })
        self.fields['image'].widget.attrs.update({  
            'class':'form-control'
            
                    
        })
        self.fields['thumbnail'].widget.attrs.update({  
            'class':'form-control'
                    
        })

class SignUpForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email','password1','password2')


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            'type':'text',  
            'placeholder':'Username',
            'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-primary-color focus:bg-white focus:ring-2 focus:ring-primary-color text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
                    
        })

        self.fields['first_name'].widget.attrs.update({
            'type':'text',  
            'placeholder':'First Name',
            'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-primary-color focus:bg-white focus:ring-2 focus:ring-primary-color text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
                    
        })

        self.fields['last_name'].widget.attrs.update({
            'type':'text',  
            'placeholder':'Last Name',
            'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-primary-color focus:bg-white focus:ring-2 focus:ring-primary-color text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
                    
        })

        self.fields['email'].widget.attrs.update({
            'type':'email',  
            'placeholder':'Email',
            'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-primary-color focus:bg-white focus:ring-2 focus:ring-primary-color text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
                    
        })

        self.fields['password1'].widget.attrs.update({
            'type':'password',  
            'placeholder':'Enter Password',
            'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-primary-color focus:bg-white focus:ring-2 focus:ring-primary-color text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
                    
        })

        self.fields['password2'].widget.attrs.update({
            'type':'password',  
            'placeholder':'Repeat Password',
            'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-primary-color focus:bg-white focus:ring-2 focus:ring-primary-color text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
                    
        })
        