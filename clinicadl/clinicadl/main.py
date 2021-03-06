from . import cli
from clinicadl.tools.deep_learning import commandline_to_json

def main():

    parser = cli.parse_command_line()
    args = parser.parse_args()

    commandline = parser.parse_known_args()

    if args.train_autoencoder:
      model_type = 'autoencoder'
    else:
      model_type = 'cnn'

    commandline_to_json(commandline, model_type)

    args.func(args)


if __name__ == '__main__':
    main()
