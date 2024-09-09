import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

data_dir = 'entries-directory'
outdir = 'output-directory'

system_message = '''
Act as an information specialist and extract data from a bibliography. 

You will be provided an XML representation of a bibliographic entry describing a periodical publication. The XML has only two elements, the root <xml> element and a <div> element that wraps a plain text representation of a bibliographic entry. The entry begins with an entry number, followed by a space, followed by a title. These are the only required fields. Other fields are optional. Below is a list of all fields that may appear in the order in which they will appear. The element name for each field is provided in angle brackets followed by a description of the element content followed by optional parsing instructions in parentheses.

All Fields:
<entry_number> Entry number 
<title> Title  
<publication_dates> Years publication began and/or ceased.  
<frequency> Frequency (most recent frequency in the case of publications with varying schedules. 
<editor> Current editor
<address> Editorial address 
<price> Subscription rates for individuals and institutions. 
<publisher> Publisher (multiple values may be present, parse each into separate element)
<pages> Number of pages in last issue and/or volume examined. 
<height> Height of the publication in centimeters.
<features> Indication if the title contains any of the following: line drawings, photographs, 
commercial advertising. (multiple values may be present, parse each into separate element)
<previous_editor> Previous editors. (multiple values may be present, parse each into separate element)
<variant_title> Variations in title, place of publication and/or frequency. (multiple values may be present, parse each into separate element)
<indexes> Indication of where the title is indexed and for what period. (See “Guide to Indexes.”) 
<microfilm> Indication if the title is available in microform and for what period. (See “Microfilm 
Sources”) 
<issn> International Standard Serials Number (ISSN). 
<lccn> Library of Congress catalog number. 
<oclc> OCLC, Inc. control number. 
<subjects> Subject focus and features. (multiple values may be present, parse each into separate element)
<holdings> Libraries holding the title, volumes and issues and/or dates held; location within library. 
<language> An indication of language(s) other than English is also included. 

Parse data as it appears into XML format using the only element names provided. 

'''

for file in os.listdir(data_dir):
  data = open(os.path.join(data_dir, file)).read()
  completion = openai.ChatCompletion.create(
    model = 'gpt-4',
    messages = [
      {'role': 'system', 'content': system_message},
      {'role': 'user', 'content': data}
    ],
    temperature = 0 
	 )
  completion_data = completion['choices'][0]['message']['content']
  out = os.path.join(outdir, file)
  with open(out, 'w') as outfile:
    outfile.write(completion_data)
    outfile.close()
