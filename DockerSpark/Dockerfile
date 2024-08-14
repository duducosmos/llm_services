FROM jupyter/pyspark-notebook:latest

USER root

# Instalar pacotes necessários
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

# Instalar o JAR do Hadoop para S3
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar -P /usr/local/spark/jars/ && \
    wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.300/aws-java-sdk-bundle-1.12.300.jar -P /usr/local/spark/jars/

# Instalar o JAR do Delta Lake
RUN wget https://search.maven.org/remotecontent?filepath=io/delta/delta-core_2.12/2.1.0/delta-core_2.12-2.1.0.jar -P /usr/local/spark/jars/

# Instalar Python requirements
COPY requirements.txt /home/jovyan/
RUN pip install -r /home/jovyan/requirements.txt

# Copiar arquivo de configuração do Spark
COPY spark-defaults.conf /usr/local/spark/conf/

COPY jupyter_lab_config.json /home/jovyan/
