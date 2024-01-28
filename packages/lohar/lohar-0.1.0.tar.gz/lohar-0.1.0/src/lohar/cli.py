# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------
import argparse
import lohar


def generate_encrypt_subparser(subparser):
    subparser.add_argument("--input", required=True, help="Input File")
    subparser.add_argument("--output", required=True, help="Output File")
    subparser.add_argument("--edition", help="Version", default=1)


def generate_decrypt_subparser(subparser):
    subparser.add_argument("--input", required=True, help="Input File")
    subparser.add_argument("--output", required=True, help="Output File")
    subparser.add_argument("--edition", help="Version", default=1)


def generate_vps_subparser(subparser):
    subparser.add_argument("--config-dir", required=True, help="Configuration Directory")
    subparser.add_argument("--instance", required=True, help="Instance Name")


def parse_cmdline():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="subcommand", required=True)
    encrypt_subparser = subparser.add_parser("encrypt", help="Encrypt a file")
    decrypt_subparser = subparser.add_parser("decrypt", help="Decrypt a file")
    setup_subparser = subparser.add_parser("vps", help="Initialize a new instance")

    generate_encrypt_subparser(encrypt_subparser)
    generate_decrypt_subparser(decrypt_subparser)
    generate_setup_subparser(vps_subparser)

    return parser.parse_args()


def main():
    args = parse_cmdline()
    if args.subcommand == "encrypt":
        lohar.crypto.encrypt(args.input, args.output, args.edition)
    elif args.subcommand == "decrypt":
        lohar.crypto.decrypt(args.input, args.output, args.edition)
    elif args.subcommand == "vps":
        if
