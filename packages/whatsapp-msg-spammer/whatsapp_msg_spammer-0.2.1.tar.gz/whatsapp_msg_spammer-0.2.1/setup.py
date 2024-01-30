from setuptools import setup, find_packages


setup(
    name="whatsapp_msg_spammer",
    version="0.2.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["whatsapp_msg_spammer = whatsapp_msg_spammer.main:main"]
    },
    install_requires=[
        "pyautogui",
        # other dependencies if needed
    ],
    python_requires=">=3.10",
)
