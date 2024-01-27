
'''
	{
		"label": "form proposal keys",
		"fields": {
			"seed": ""
		}
	}
'''

import moneti.treasury.climate as treasury_climate

def play (
	JSON
):
	paths = treasury_climate ["paths"]

	fields = JSON ["fields"]
	seed = fields ["seed"]
	directory_path = fields ["directory_path"]

	print (
	
	)

	import moneti.modules.proposals.keys.form as form_proposal_keys
	form_proposal_keys.smoothly (
		#
		#	inputs, consumes, utilizes
		#
		utilizes = {
			"seed": seed
		},
		
		#
		#	outputs, produces, builds
		#
		builds = {
			"seed": {
				"path": normpath (join (directory_path, "proposal.seed"))
			},
			"private key": {
				"format": "hexadecimal",
				"path": normpath (join (directory_path, "proposal.private_key.hexadecimal"))
			},
			"public key": {
				"format": "hexadecimal",
				"path": normpath (join (directory_path, "proposal.public_key.hexadecimal"))
			}
		}
	)