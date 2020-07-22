FROM kalilinux/kali-rolling

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Or your actual UID, GID on Linux if not the default 1000
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Configure apt and install packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -y install git procps lsb-release \
    #
    # Install python + pip
    && apt-get install python3 python3-pip -y \
    #
    # Install project specific apt packages
    && apt-get install nikto nmap sslscan sslyze -y \
    #
    # Install patched version of python-nmap
    && git clone https://github.com/JakobRPennington/python-nmap.git /workspace/python-map \
    && cd /workspace/python-map \
    && python3 setup.py install \
    #
    # Install pylint
    && pip3 --disable-pip-version-check --no-cache-dir install pylint \
    #
    # Update Python environment based on requirements.txt (if presenet)
    && if [ -f "/tmp/pip-tmp/requirements.txt" ]; then pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt; fi \
    && rm -rf /tmp/pip-tmp \
    #
    # Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=

# Set up environment variables
RUN export LC_CTYPE=en_US.UTF-8 \
    && export LC_ALL=en_US.UTF-8 \
    && export LANGUAGE=en_US.UTF-8
