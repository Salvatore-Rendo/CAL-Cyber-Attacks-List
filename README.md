<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="src/logo.png" alt="Project logo"></a>
</p>

<h3 align="center">CAL Cyber Attacks List </h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Salvatore-Rendo/CAL-Cyber-Attacks-List.svg)](https://github.com/Salvatore-Rendo/CAL-Cyber-Attacks-List/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Salvatore-Rendo/guardianpy.svg)](https://github.com/Salvatore-Rendo/CAL-Cyber-Attacks-List/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A list of cyber Attacks made with Python or C
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [⚠️ Warning ](#️-warning-)
- [🏁 Getting Started ](#-getting-started-)
  - [Installing](#installing)
- [🎈 Usage ](#-usage-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)

## 🧐 About <a name = "about"></a>

A list of cyber Attacks mad with Python or C, feel free to check it out

## ⚠️ Warning <a name = "about"></a>

**DISCLAIMER: THIS IS AN EXAMPLE FOR PRACTICING CYBERSECURITY-RELATED TOPICS**

This repository is solely intended for educational and practice purposes related to cybersecurity. It is NOT meant to be used for any malicious or illegal activities. 

**Please note:**

- Do not use this software or any information provided here with malicious intent.
- This repository is meant for educational purposes to enhance cybersecurity knowledge and skills.
- I do not endorse, encourage, or support any form of illegal or unethical activities.

Remember to use the knowledge gained from this repository responsibly and in compliance with applicable laws and regulations.

**Contributors:** If you contribute to this repository, you are expected to follow the guidelines, which align with these principles.

This disclaimer is intended to make my stance on the responsible and ethical use of cybersecurity knowledge clear. If you have any questions or concerns, please feel free to reach out.

Thank you for understanding and adhering to these principles.

## 🏁 Getting Started <a name = "getting_started"></a>

### Installing


```
git clone https://github.com/Salvatore-Rendo/CAL-Cyber-Attacks-List
```

```
cd CAL-Cyber-Attacks-List
```

```
pip3 install -r requirements.txt
```

## 🎈 Usage <a name="usage"></a>

Change directory inside the projects to chose the attack you want to use:

```
cd Attack-you-chose
```

Then run the helper to get a better understanding of the attack

```
python3 attack-you-chose.py -h
```

If the attack requires a target ip, you can easily create a dummy server with python:

```
python3 -m http.server [port to listen eg.4343]
```
Or with netcat:
```
nc -lk [port to listen eg.4343]
```

And use it to be the target of your attacks.

I recommend using a network analyzer (e.g., [Wireshark](https://www.wireshark.org/)) to observe the results of the attacks and to analyze the types of traffic they generate.


## ⛏️ Built Using <a name = "built_using"></a>


- [Python](https://www.python.org/) - Framework
- [Flaticon](https://www.flaticon.com/) Icon


## ✍️ Authors <a name = "authors"></a>

- [@Salvatore-Rendo](https://github.com/Salvatore-Rendo) - Idea & Initial work


