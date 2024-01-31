from setuptools import setup, find_packages
import platform

architecture = platform.machine()
is_arm = 'arm' in architecture.lower() or architecture == 'aarch64'

if not is_arm:
    requires=[
        "numpy",
        "onnx",
        "onnxruntime",
        "onnxruntime-extensions",
        "transformers",
        "faiss-cpu",
        "torch",
        "pytest",
        "pytest-cov",
        "rank-bm25",
        "thefuzz[speedup]"
    ]
else:
    requires=[
        "numpy",
        "transformers",
        "faiss-cpu",
        "torch",
        "pytest",
        "pytest-cov",
        "rank-bm25",
        "thefuzz[speedup]"
    ]

setup(
    name='minivectordb',
    version='1.1.8',
    author='Carlo Moro',
    author_email='cnmoro@gmail.com',
    description="This is a Python project aimed at extracting embeddings from textual data and performing semantic search.",
    packages=find_packages(),
    package_data={
        'minivectordb': ['resources/embedding_model_quantized.onnx']
    },
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)