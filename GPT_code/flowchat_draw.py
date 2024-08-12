from graphviz import Digraph

# Create a Digraph object with Korean labels
dot_korean = Digraph(comment='PCB 검사 프로세스 플로우 차트')

# Set the font for Korean text to a common Korean font
dot_korean.attr(fontname='Malgun Gothic')

# Define the nodes and their labels in Korean
dot_korean.node('A', '+ 버튼 누르기', shape='rectangle', style='filled', fillcolor='#ff99ff', fontname='Malgun Gothic')
dot_korean.node('B', 'PRODUCT_STATE 테이블 작성\n(PRODUCT_ID, INSPECTION_START_TIME)', shape='rectangle', style='filled', fillcolor='#bbccff', fontname='Malgun Gothic')
dot_korean.node('C', '검사 중', shape='rectangle', style='filled', fillcolor='#bbccff', fontname='Malgun Gothic')
dot_korean.node('D', '웹캠으로 검사 수행', shape='rectangle', style='filled', fillcolor='#bbccff', fontname='Malgun Gothic')
dot_korean.node('E', '* 버튼 누르기', shape='rectangle', style='filled', fillcolor='#ff99ff', fontname='Malgun Gothic')
dot_korean.node('F', '프레임 이미지 캡처', shape='rectangle', style='filled', fillcolor='#bbccff', fontname='Malgun Gothic')
dot_korean.node('G', 'YOLO로 처리', shape='rectangle', style='filled', fillcolor='#bbccff', fontname='Malgun Gothic')
dot_korean.node('H', 'INSPECT_STATE 테이블 작성\n(PRODUCT_ID, ERROR_TYPE, WIDTH, HEIGHT)', shape='rectangle', style='filled', fillcolor='#bbccff', fontname='Malgun Gothic')
dot_korean.node('I', '- 버튼 누르기', shape='rectangle', style='filled', fillcolor='#ff99ff', fontname='Malgun Gothic')
dot_korean.node('J', 'PRODUCT_STATE 테이블 업데이트\n(INSPECTION_COMPLETE_TIME, IS_DEFECT)', shape='rectangle', style='filled', fillcolor='#bbccff', fontname='Malgun Gothic')
dot_korean.node('K', '종료', shape='rectangle', style='filled', fillcolor='#ff99ff', fontname='Malgun Gothic')

# Define the edges between the nodes
dot_korean.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IJ', 'JK'])

# Render the graph to a file and save as an image
flowchart_path_korean = './data/PCB_Inspection_Process_Flowchart_Korean_Font.png'
dot_korean.render(flowchart_path_korean, format='png', cleanup=True)

flowchart_path_korean
