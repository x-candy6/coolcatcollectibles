from django import forms
from .models import Product


class ProductFilterForm(forms.Form):
    # Price Range
    # Publisher
    # Year
    # Series
    # Character

    publisher_list = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=[], required=False)
    year_list = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=[], required=False)
    series_list = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=[], required=False)

    def __init__(self, *args, **kwargs):
        pub_options = kwargs.pop('pub_options', [])
        year_options = kwargs.pop('year_options', [])
        series_options = kwargs.pop('series_options', [])
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        self.fields['publisher_list'].choices = [
            (pub, pub) for pub in pub_options]

        self.fields['year_list'].choices = [
            (year, year) for year in year_options]

        self.fields['series_list'].choices = [
            (series, series) for series in series_options]

    # def clean(self):
    #    cleaned_data = super().clean()
    #    selected_publisher = cleaned_data.get('publisher_list')
    #    selected_series = cleaned_data.get('series_list')
    #    selected_years = cleaned_data.get('years_list')
    #    if not selected_series:
    #        cleaned_data['series_list'] = None
    #    if not selected_years:
    #        cleaned_data['year_list'] = None
    #    if not selected_publisher:
    #        cleaned_data['publisher_list'] = None

    #    return cleaned_data
