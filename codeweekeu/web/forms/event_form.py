# -*- coding: utf-8 -*-
from django import forms
from django.utils.html import escape
from django_countries import countries
from api.models import Event
from taggit.forms import TagField


class AddEvent(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'organizer', 'description', 'location', 'country', 'start_date', 'end_date',
		          'event_url', 'contact_person', 'picture','tags']
		labels = {
			'title': 'Your event\'s title:',
			'organizer': 'Who\'s organizing this event?',
			'description': 'Short event description:',
		    'location': 'Where will the event be taking place?',
		    'country': 'Event\'s country:',
		    'start_date': 'When does the event start?',
		    'end_date': 'When does the event end?',
		    'event_url': 'Do you have a website with more information about the event? (optional)',
		    'contact_person': 'Would you like to display a contact email? (optional)',
		    'picture': 'You can also upload an image to represent your event: (optional)',
		   	'tags': 'Tags, separated by commas:',
		}
		error_messages = {
			'title': {
				'required': u'Please enter a title for your event.',
				'invalid': u'Can you please check if this is a valid title?',
			},
			'organizer': {
				'required': u'Please enter an organizer.',
				'invalid': u'Can you please check if this is a valid organizer?',
			},
			'description': {
				'required': u'Please write a short description of what the event is about.',
				'invalid': u'Please check if the description only contains regular text.',
			},
		    'location': {
				'required': u'Please enter a location or use online for web-based events.',
				'invalid': u'Please check your event\'s location',
			},
		    'country': {
				'required': u'Please select the event\'s country.',
				'invalid': u'Make sure the event country is written in English.',
			},
		    'start_date': {
				'required': u'Please enter a valid date and time.',
				'invalid': u'This doesn\'t seem like a valid date and time. Can you check, please?',
			},
		    'end_date': {
				'required': u'Please enter a valid date and time.',
				'invalid': u'This doesn\'t seem like a valid date and time. Can you check, please?',
			},
			'event_url': {
				'invalid': u'Please enter a valid web address starting with http://',
			},
		    'contact_person': {
				'invalid': u'Please enter a valid email address.',
			},
		    'picture': {
				'invalid': u'Make sure this is a valid image.',
			},
			'tags': {
				'required': u'Please type in some tags to categorize the target audience and type of event',
				'invalid': u'Please enter tags in plain text, separated by commas.',
			},
		}


class AddEvent1(forms.Form):
	title = forms.CharField(
		required=True,
		max_length=100,
		label='Your event\'s title:',
		widget=forms.widgets.TextInput(),
		error_messages={
		'required': u'Please enter a title for your event.',
		'invalid': u'Can you please check if this is a valid title?',
		},
	)

	organizer = forms.CharField(
		required=True,
		max_length=140,
		label='Who\'s organizing this event?',
		widget=forms.widgets.TextInput(),
		error_messages={
		'required': u'Please enter an organizer.',
		'invalid': u'Can you please check if this is a valid organizer?',
		},
	)

	description = forms.CharField(
		required=True,
		label='Short event description:',
		widget=forms.widgets.Textarea(),
		error_messages={
		'required': u'Please write a short description of what the event is about.',
		'invalid': u'Please check if the description only contains regular text.',
		},
	)

	location = forms.CharField(
		required=True,
		label='Where will the event be taking place?',
		widget=forms.widgets.TextInput(),
		error_messages={
		'required': u'Please enter a location or use online for web-based events.',
		'invalid': u'Please check your event\'s location',
		},
	)

	country = forms.ModelChoiceField(
		required=True,
		label='Event\'s country:',
		widget=forms.widgets.Select(),
		queryset=countries, #CountryList.objects.all(),
		error_messages={
		'required': u'Please select the event\'s country.',
		'invalid': u'Make sure the event country is written in English.',
		},
	)

	start_date = forms.DateTimeField(
		required=False,
		label='When does the event start?',
		error_messages={
		'required': u'Please enter a valid date and time.',
		'invalid': u'This doesn\'t seem like a valid date and time. Can you check, please?',
		},
	)

	end_date = forms.DateTimeField(
		required=False,
		label='When does the event end?',
		error_messages={
		'required': u'Please enter a valid date and time.',
		'invalid': u'This doesn\'t seem like a valid date and time. Can you check, please?',
		},
	)

	event_url = forms.URLField(
		required=False,
		label='Do you have a website with more information about the event? (optional)',
		error_messages={
		'invalid': u'Please enter a valid web address starting with http://',
		},
	)

	contact_person = forms.EmailField(
		required=False,
		label='Would you like to display a contact email? (optional)',
		error_messages={
		'invalid': u'Please enter a valid email address.',
		},
	)

	picture = forms.ImageField(
		required=False,
		label='You can also upload an image to represent your event: (optional)',
		error_messages={
		'invalid': u'Make sure this is a valid image.',
		},
	)

	def is_valid(self):
		form = super(AddEvent, self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all__':
				error = escape(str(error))
				self.fields[f].widget.attrs.update({'class': 'error', })
		return form
