from setuptools import setup, find_packages  

setup(  
    name="your_package_name",  # Replace with your package name  
    version="1.0.1",           # Package version  
    description="Your package description",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    author="Your Name",  
    author_email="your_email@example.com",  
    url="https://github.com/your_username/your_package_name",  
    packages=find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",  
    ],  
    python_requires=">=3.6",  # Specify the minimum Python version  
    install_requires=[],      # List your dependencies here  
)  
