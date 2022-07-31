Vagrant.configure(2) do |config|

    # main & default: normal OS series...
    config.vm.define "main", primary: true do |node|
        node.vm.box = "alvistack/centos-8-stream"


        node.vm.provision "ansible" do |ansible|
            ansible.playbook = "test.yml"
            #ansible.sudo = true
            ###ansible.verbose = "vvv"
        end

        # Prometheus server UI port
        node.vm.network :forwarded_port, guest: 9090, host: 7090

        node.vm.network :forwarded_port, guest: 80, host: 8080

       node.vm.provider "virtualbox" do |vb|
          vb.customize ["modifyvm", :id, "--memory", "1024"]
       end

    end

end

