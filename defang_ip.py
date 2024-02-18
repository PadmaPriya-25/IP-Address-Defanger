def ip_address(ip):
    defanged_address = ip.replace('.', '[.]')
    return defanged_address

def main():
    user_ip = input("Enter an IP address: ")
    defanged_ip = ip_address(user_ip)
    print("Original IP address:", user_ip)
    print("Defanged IP address:", defanged_ip)

if __name__ == "__main__":
    main()
