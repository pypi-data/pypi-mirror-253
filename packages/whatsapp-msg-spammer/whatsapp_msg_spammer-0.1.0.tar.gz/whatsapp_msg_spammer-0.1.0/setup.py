from setuptools import setup, find_packages


setup(
    name="whatsapp_msg_spammer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["whatsapp_msg_spammer = whatsapp_msg_spammer.main:main"]
    },
    python_requires=">=3.10",
)
