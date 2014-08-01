apt-get update
apt-get -y install git python-virtualenv software-properties-common python-software-properties curl vim
add-apt-repository -y ppa:webupd8team/java
apt-get update

echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
apt-get -y install libxtst6 oracle-java7-installer
apt-get -q -y install oracle-java7-set-default
