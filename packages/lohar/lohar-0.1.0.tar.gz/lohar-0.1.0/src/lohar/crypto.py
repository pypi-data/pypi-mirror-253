# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import os
import subprocess
import getpass


def config_v1(input_file, output_file):
    command = ["openssl", "enc"]
    command.append("-aes-256-cbc")
    command.append("-pbkdf2")
    command.append("-md")
    command.append("sha512")
    command.append("-iter")
    command.append("1000000")
    password = getpass.getpass("Enter Password: ")
    command.append("-k")
    command.append(password)
    command.append("-in")
    command.append(input_file)
    command.append("-out")
    command.append(output_file)
    return command


def encrypt(input_file, output_file, edition):
    if edition == 1:
        command = encrypt_v1(input_file, output_file)
    else:
        raise NotImplementedError("Edition {} not implemented".format(edition))
    subprocess.run(command)


def encrypt_v1(input_file, output_file):
    command = config_v1(input_file, output_file)
    command.append("-e")
    return command


def decrypt(input_file, output_file, edition):
    if edition == 1:
        command = decrypt_v1(input_file, output_file)
    else:
        raise NotImplementedError("Edition {} not implemented".format(edition))

    subprocess.run(command)


def decrypt_v1(input_file, output_file):
    command = config_v1(input_file, output_file)
    command.append("-d")
    return command
