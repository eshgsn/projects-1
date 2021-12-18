from django.db import models
# Create your models here.
class StudentProjectModel(models.Model):
    name = models.CharField(
        max_length=30,blank=False,null=False
    )
    studentId = models.CharField(
        max_length=15, blank=False, null=False,primary_key = True
    )

    topic_list = [
    ('Question Answering System for Machine Intelligent','Question Answering System for Machine Intelligent'),
    ('Building a Quantum Classifier using Quantum Computing','Building a Quantum Classifier using Quantum Computing'),
    ('Influence Maximization in Social Networks','Influence Maximization in Social Networks'),
    ('Link Prediction in Dynamic Networks','Link Prediction in Dynamic Networks'),
    ('Recommender Systems','Recommender Systems'),
    ('Machine Learning based Applications','Machine Learning based Applications'),
    ('Deep Learning based Applications','Deep Learning based Applications'),
    ('Machine learning','Machine learning'),
    ('IoT','IoT'),
    ('5G','5G'),
    ('BCI','BCI'),
    ('Anomaly detection in video surveillance','Anomaly detection in video surveillance'),
    ('Physical distance maintaining among the crowd in Deep Learning','Physical distance maintaining among the crowd in Deep Learning'),
    ('Crowd Motion Analysis in Deep Learning','Crowd Motion Analysis in Deep Learning'),
    ('Emotion Recognition with voice input','Emotion Recognition with voice input'),
    ('Credit Card Fraud Detection','Credit Card Fraud Detection'),
    ('Water Quality Monitoring For Disease Prediction','Water Quality Monitoring For Disease Prediction'),
    ('Algorithmic mechanism design for resource allocation in cloud computing','Algorithmic mechanism design for resource allocation in cloud computing'),
    ('Resource allocation and pricing in cloud','Resource allocation and pricing in cloud'),
    ('Market based approach for resource allocation in Fog computing','Market based approach for resource allocation in Fog computing'),
    ('Game theoretic solutions to medical imaging','Game theoretic solutions to medical imaging'),
    ('Game theoretic approach for fair resource allocation P2P network','Game theoretic approach for fair resource allocation P2P network'),
    ('Different machine learning schemes for land cover classification using Remote sensing','Different machine learning schemes for land cover classification using Remote sensing'),
    ('Land cover classification using GIS and RS','Land cover classification using GIS and RS'),
    ('Applications of Graph Database','Applications of Graph Database'),
    ('Comparison of Big Data Tools','Comparison of Big Data Tools'),
    ('Data Mining Algorithms','Data Mining Algorithms'),
    ('Data Analytics','Data Analytics'),
    ('AI problem solving using graph database','AI problem solving using graph database'),
    ('Applications of next generation databases','Applications of next generation databases'),
    ('Machine Learning-Based Model to Predict the Disease Severity and Outcome in COVID-19 and Black Fungus Patients','Machine Learning-Based Model to Predict the Disease Severity and Outcome in COVID-19 and Black Fungus Patients'),
    ('Using Deep learning Predict the Disease Severity and Outcome in different types Anaemic Patients','Using Deep learning Predict the Disease Severity and Outcome in different types Anaemic Patients'),
    ('Information security','Information security'),
    ('Authentication protocols','Authentication protocols'),
    ('Access control protocols','Access control protocols'),
    ('Blockchain technology','Blockchain technology'),
    ('Security protocols in Internet of Things','Security protocols in Internet of Things'),
    ('Malware detection and analysis','Malware detection and analysis'),
    ('Cyber threats analysis and hunting','Cyber threats analysis and hunting'),
    ('Biometric security system','Biometric security system')
]

    projectChoose = models.CharField(
        max_length=150,blank=False,null=False,
        choices=topic_list
    )

    # gender_choices = [
    #     ('male', "Male"),
    #     ("female", "Female"),
    # ]
    # gender = models.CharField(
    #     max_length=6, blank=False, null=False,
    #     choices=gender_choices,
    # )
    def __str__(self):
        return self.name


