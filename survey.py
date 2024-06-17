import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
def pic1():
    dataset = pd.read_csv("heart1.csv")
    save_folder = "static/plots"
    os.makedirs(save_folder, exist_ok=True)
    target_counts = dataset['target'].value_counts()
    fig, ax = plt.subplots()
    labels = ['No Heart Disease (0)', 'Heart Disease (1)']
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0) 
    ax.pie(target_counts, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False, colors=colors, explode=explode)
    ax.axis('equal')
    plt.title("Distribution of Heart Disease")
    os.makedirs(save_folder, exist_ok=True)
    save_path = os.path.join(save_folder, "main.png")
    plt.savefig(save_path)
    
    subset = dataset[dataset['sex'] == 0]
    counts = subset['target'].value_counts()
    fig, ax = plt.subplots()
    labels = ["No Heart Disease", "Heart Disease"]
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.axis('equal')
    plt.title(" heart disease people in male ")
    save_path = os.path.join(save_folder, "male.png") 
    plt.savefig(save_path)
    
    subset = dataset[dataset['sex'] == 1]
    counts = subset['target'].value_counts()
    fig, ax = plt.subplots()
    labels = ["No Heart Disease", "Heart Disease"]
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.axis('equal')
    plt.title("heart disease people in female ")
    save_path = os.path.join(save_folder, "female.png")
    plt.savefig(save_path)
    
    subset = dataset[dataset['target'] == 1]
    counts = subset['sex'].value_counts()
    fig, ax = plt.subplots()
    labels = ["female", "male"]
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.axis('equal')
    plt.title(" heart disease people in sex")
    save_path = os.path.join(save_folder, "heart_disease_in_sex.png")
    plt.savefig(save_path)

    

def pic():
    dataset = pd.read_csv("heart1.csv")
    save_folder = "static/plots"
    os.makedirs(save_folder, exist_ok=True)
    y = dataset["target"]
    cp_values = dataset["cp"]
    ax = sns.barplot(x=cp_values, y=y)
    custom_labels = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
    ax.set_xticklabels(custom_labels)
    plt.title("Chest Pain Type vs Target")
    plt.xlabel("Chest Pain Type")
    plt.ylabel("Target")
    save_path = os.path.join(save_folder, "cp.png")
    plt.savefig(save_path)

    y = dataset["chol"]
    cp_values = dataset["target"]
    ax = sns.barplot(x=cp_values, y=y)
    custom_labels = ["0","1"]
    ax.set_xticklabels(custom_labels)
    plt.title("Number of Major vessels")
    plt.ylabel("Target")
    save_path = os.path.join(save_folder, "chol.png")
    plt.savefig(save_path)


    y = dataset["ca"]
    cp_values = dataset["target"]
    ax = sns.barplot(x=cp_values, y=y)
    custom_labels = ["0","1"]
    ax.set_xticklabels(custom_labels)
    plt.title("chol Type vs Target")
    plt.xlabel("chol")
    plt.ylabel("Target")
   
  
    save_path = os.path.join(save_folder, "ca.png")
    plt.savefig(save_path)



    y = dataset["thal"]
    cp_values = dataset["target"]
    ax = sns.barplot(x=cp_values, y=y)
    custom_labels = ["0","1"]
    ax.set_xticklabels(custom_labels)
    plt.title("Thalassemia Type vs Target")
    plt.xlabel("Thalassemia")
    plt.ylabel("Target")
    save_path = os.path.join(save_folder, "thal.png")
    plt.savefig(save_path)

