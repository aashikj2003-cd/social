#!/usr/bin/env python

"""
SocialEngineer - Social Engineering Toolkit
-------------------------------------------

Author      : TEAM PPS
GitHub      : 
Project     : SocialEngineer - An all-in-one CLI framework for social engineering

License     : Open-source — strictly for educational and ethical hacking purposes ONLY.

Note to Users:
--------------
🔐 This tool is intended solely for educational use, research, and authorized security testing.
🚫 Unauthorized use of this tool on networks you do not own or lack permission to test is illegal.
❗ If you use or modify this code, PLEASE GIVE PROPER CREDIT to the original author.

Warning to Code Thieves:
------------------------
❌ Removing this header or claiming this project as your own without credit is unethical and violates open-source principles.
🧠 Writing your own code earns respect. Copy-pasting without attribution does not.
✅ Be an ethical hacker. Respect developers' efforts and give credit where it’s due.
"""



from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os


console = Console()


def clear():
    os.system("clear")

def show_banner():
    os.system("clear")
    ascii_art = """
                                                                                                    v2.0

███████╗ ██████╗  ██████╗██╗ █████╗ ██╗         ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗███████╗██████╗ 
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║         ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝██╔════╝██╔══██╗
███████╗██║   ██║██║     ██║███████║██║         █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  █████╗  ██████╔╝
╚════██║██║   ██║██║     ██║██╔══██║██║         ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔══██╗
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗    ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝                                                                                                                                                                                                                        
                                                               [bold green] Author: TEAM PPS
                                                                Website:                                                                 
                                                     
"""
    console = Console()
    console.print(ascii_art, style="bold cyan")
    

def show_credentials():
    clear()
    table = Table(title="[bold magenta]Captured Credentials[/bold magenta]", show_header=True, header_style="bold blue")
    table.add_column("Username", style="bold green")
    table.add_column("Password")
    table.add_column("Date/Time")
    table.add_column("Template")
    table.add_column("Client IP")
    table.add_column("Device Info")

    creds = get_credentials_json()
    for c in creds:
        table.add_row(c['username'], c['password'], c['datetime'], c['template'], c['useragent'], c['ip'])
    show_banner()
    console.print(table)
    console.input("\n[bold yellow]↩️ Press Enter to go back... [/bold yellow]")


def nowifi():
    console.print("[bold red]❌ No WiFi interfaces found![/bold red]")
    exit()

def wifi_available(interfaces):
    options = "\n".join([f"{i+1}. [cyan]{iface}[/cyan]" for i, iface in enumerate(interfaces)])
    options += "\n0. [bold red]Back to Main Menu[/bold red]"
    console.print(Panel.fit(f"📡 [bold yellow]Available WiFi Interfaces:[/bold yellow]\n\n{options}", title="Choose Interface", style="bold green"))


def invalid_Selection():
    console.print("[bold red]❌ Invalid selection![/bold red]")

def bye():
    console.print("[red]👋 Goodbye![/red]")

def not_implemented():
    print("\n[red]❌ Option not implemented yet.[/red]")


def credentials(cred):

            console.print(Panel.fit(f"""
[bold green]Captured Credentials[/bold green]
[bold]Username:[/bold] {cred.get("username")}
[bold]Password:[/bold] {cred.get("password")}
[bold]Time    :[/bold] {cred.get("datetime")}
[bold]IP      :[/bold] {cred.get("ip")}
[bold]UserAgent:[/bold] {cred.get("useragent")}
""", title="🔐 New Login", border_style="green"))
            

def wifiphish(inf,attack_mode,wifiname):
     console.print(Panel.fit(f"""
[bold]Attack Mode:[/bold] {attack_mode}
[bold]Device     :[/bold] {inf}
[bold]Wifi Name  :[/bold] {wifiname}
[bold]Stop       :[/bold] CTRL+C 
""", title="🚨 Launching Wifi Attack", border_style="red"))
     
def wifispam(interface, attack_mode, ssid_name, ssid_count):
     console.print(Panel.fit(f"""
[bold]Attack Mode:[/bold] {attack_mode}
[bold]Device     :[/bold] {interface}
[bold]Wifi Name  :[/bold] {ssid_name}
[bold]Wifi count :[/bold] {ssid_count}
[bold]Stop       :[/bold] CTRL+C 
""", title="🚨 Launching Wifi Attack", border_style="red"))
     

def show_wifi_targets(wifi_targets):
    show_banner()
    menu = ["📡 [bold yellow]Available WiFi Targets:[/bold yellow]\n"]
    
    for i, (bssid, essid, channel) in enumerate(wifi_targets, start=1):
        menu.append(f"[cyan]{i}.[/cyan] [bold white]{essid:<25}[/bold white] [dim]{bssid}[/dim]")
    
    menu.append("[bold red]0.[/bold red] Back to Main Menu")
    panel_content = "\n".join(menu)
    
    console.print(Panel.fit(panel_content, title="[bold green]Choose Target[/bold green]", style="bold green"))



def ipc_banner():
    console.print(Panel.fit(
        "[bold green]IP Changer[/bold green]",
        border_style="red"
    ))

def ipchanger_instructions(): 
     console.print(Panel.fit( "[bold yellow]IP Changer Instructions[/bold yellow]\n\n" "👉 This tool uses the Tor service to change your public IP.\n" "👉 Enter the interval in seconds for IP rotation (minimum 5 seconds).\n" "👉 During IP change, Tor may throw errors depending on your network or machine configuration.\n" "👉 Use this tool only for educational purposes.\n" "👉 To use in a browser, configure the proxy in Firefox with [bold]IP: 127.0.0.1[/bold] and [bold]Port: 9050[/bold].\n" "❌ Enter [red]'x'[/red] to exit anytime.", border_style="magenta" ))
