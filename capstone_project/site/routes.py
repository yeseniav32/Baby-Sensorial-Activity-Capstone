from flask import Blueprint, render_template;

site = Blueprint('site',__name__, template_folder='site_templates')

@site.route('/') #base/main page
def home():
    return render_template('index.html')


# ACTIVITES PAGES
@site.route('/visual-activities') 
def visualActivities():
    return render_template('visual.html')

@site.route('/hearing-activities') 
def hearingActivities():
    return render_template('hearing.html')

@site.route('/smell-activities') 
def smellActivities():
    return render_template('smell.html')

@site.route('/touch-activities') 
def touchActivities():
    return render_template('touch.html')