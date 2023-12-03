from json import dumps
from time import localtime
from datetime import datetime

from argparse import Namespace

from utils.validation import is_output_file_valid
    

def output_file(args: Namespace, dest='../data/data_source.tsv'):
  filename = args.output
  if not is_output_file_valid(filename):
    raise ValueError('Filename is invalid!')
  
  command = args.command
  
  t = localtime()
  timestamp = str(datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))
  output = {
    'timestamp': timestamp,
    'datasource': dest,
    'command': f'-{command}',
    'arguments': [
      {
        'command': '-output',
        'options': {
          'output': f'./src/logs/{filename}'
        }
      }
    ]
  }

  val = {
    'command': f'-{command}',
    'options': {}
  }
  for key, value in args.__dict__.items():
    val['options'].update({ key: value }) if key in ['medals', 'total', 'overall', 'interactive', 'countries', 'year', 'country', 'top'] else False
    output['arguments'].append(val)

  output['arguments'] = output['arguments'][:2][::-1]
  
  with open(f'./src/logs/{filename}', 'a') as output_file:
    output_file.write(dumps(output, indent=3))
    output_file.write('\n' + '-' * 50 + '\n\n')
