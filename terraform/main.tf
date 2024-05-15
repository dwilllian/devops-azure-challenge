
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg_prd" {
  name     = "RGDesafio"
  location = "East US"
}

resource "azurerm_virtual_network" "rede_prd" {
  name                = "rede_prd"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg_prd.location
  resource_group_name = azurerm_resource_group.rg_prd.name
}

resource "azurerm_subnet" "sub_rede" {
  name                 = "SB_privado"
  resource_group_name  = azurerm_resource_group.rg_prd.name
  virtual_network_name = azurerm_virtual_network.rede_prd.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_network_interface" "int_rede" {
  name                = "nic_VM"
  location            = azurerm_resource_group.rg_prd.location
  resource_group_name = azurerm_resource_group.rg_prd.name

  ip_configuration {
    name                          = "privado_server"
    subnet_id                     = azurerm_subnet.sub_rede.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "vm_desafio" {
  name                = "vmDesafio"
  resource_group_name = azurerm_resource_group.rg_prd.name
  location            = azurerm_resource_group.rg_prd.location
  size                = "Standard_DS1_v2"

  admin_username = "admin"
  admin_password = "admin"

  network_interface_ids = [
    azurerm_network_interface.int_rede.id,
  ]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
