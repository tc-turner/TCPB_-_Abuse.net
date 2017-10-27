"""
 Copyright 2017 ThreatConnect, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
"""

""" third party """
import dns.resolver

""" custom """
from tcex import TcEx

tcex = TcEx()

tcex.parser.add_argument(
    '--host_to_search', help='Host To Lookup', required=True)

# get args
args = tcex.args



def main():
    """ Main PB App Entrypoint """
    try:
        host = tcex.playbook.read_string(args.host_to_search)
        abusenet = "{}.{}".format(host,"contacts.abuse.net")
        answers = dns.resolver.query(abusenet, 'TXT')
        str_array = []
        for rdata in answers:
            str_array.append(rdata.to_text().strip('"'))
        print str_array
        print host
        tcex.playbook.create_output("abuse.contacts", str_array)
        tcex.log.debug("Got results {}".format(str_array))
    except Exception as e:
        tcex.log.error(e.message)
        tcex.playbook.create_output('abuse.debug', e.message)
        tcex.exit(1)

if __name__ == "__main__":
    main()
