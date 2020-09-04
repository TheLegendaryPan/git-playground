Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

	config.vm.network "forwarded_port", guest: 5000, host: 5000
	config.vm.provision "shell", privileged: false, inline: <<-SHELL     
		sudo apt-get update 
		#install pre-req
		sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
		libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
		xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
		
		git clone https://github.com/pyenv/pyenv.git ~/.pyenv
		echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
		echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
		echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
		
		#install pip then python, otherwise pyenv install hangs
		sudo apt-get -y install python-pip
		#exec "$SHELL"
	SHELL
	config.vm.provision "shell", privileged: false, path: "provision/python-setup.sh"
	config.vm.provision "shell", privileged: false, path: "provision/poetry-setup.sh"
	
	
	## No need to clone my repo. find a way to sync up my folder from local git-playground to the VM
	## then save the pyproject.toml file over to my local repo so it gets copied over. 
	config.trigger.after :up do |trigger|     
		trigger.name = "Launching App"     
		trigger.info = "Running the TODO app setup script"     
		trigger.run_remote = {privileged: false, inline: "
		# Install dependencies and launch
		cd /vagrant
		poetry update
		poetry install
		# starting the app
		nohup poetry run flask run --host=0.0.0.0 > log.txt 2>&1 &
		#poetry run flask run --host=0.0.0.0 ##0.0.0.0 is needed to allow access
		"}
	end
	
end
