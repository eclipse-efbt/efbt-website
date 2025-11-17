#!/usr/bin/env python3
"""
Markdown to HTML Converter (No External Libraries)
Converts all markdown files in markdown_content/ directory to HTML files,
preserving the directory structure but removing the markdown_content/ prefix.
Uses the website's styling with navbar and footer includes.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# Configuration for disabled guides (coming soon pages)
DISABLED_GUIDES = [
    'define-executable-tests'
]


class MarkdownToHTMLConverter:
    """Simple markdown to HTML converter without external dependencies."""

    def __init__(self):
        self.list_stack = []
        self.in_code_block = False
        self.in_table = False
        self.used_ids = set()  # Track used heading IDs to prevent duplicates

    def convert(self, markdown_text):
        """Convert markdown text to HTML."""
        lines = markdown_text.split('\n')
        html_lines = []
        i = 0

        while i < len(lines):
            line = lines[i]

            # Handle code blocks
            if line.strip().startswith('```'):
                if not self.in_code_block:
                    self.in_code_block = True
                    lang = line.strip()[3:].strip()
                    html_lines.append('<pre><code>')
                else:
                    self.in_code_block = False
                    html_lines.append('</code></pre>')
                i += 1
                continue

            if self.in_code_block:
                # Escape HTML characters in code blocks
                escaped_line = self.escape_html(line)
                html_lines.append(escaped_line)
                i += 1
                continue

            # Process the line
            converted_line = self.convert_line(line)

            # Handle lists
            converted_line = self.handle_lists(converted_line, line)

            # Handle tables
            if self.is_table_line(line):
                if not self.in_table:
                    self.in_table = True
                    html_lines.append('<table class="table table-bordered">')
                converted_line = self.convert_table_row(line)
            elif self.in_table and not self.is_table_line(line):
                self.in_table = False
                html_lines.append('</table>')

            if converted_line:
                html_lines.append(converted_line)

            i += 1

        # Close any open lists
        while self.list_stack:
            tag = self.list_stack.pop()
            html_lines.append(f'</{tag}>')

        # Close table if still open
        if self.in_table:
            html_lines.append('</table>')

        return '\n'.join(html_lines)

    def escape_html(self, text):
        """Escape HTML special characters."""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))

    def convert_line(self, line):
        """Convert a single line of markdown to HTML."""
        if not line.strip():
            return ''

        # Headers
        if line.startswith('#'):
            return self.convert_header(line)

        # Horizontal rule
        if re.match(r'^[\-\*_]{3,}$', line.strip()):
            return '<hr>'

        # Blockquote
        if line.startswith('>'):
            content = line[1:].strip()
            return f'<blockquote>{self.convert_inline(content)}</blockquote>'

        # List items are handled separately
        if re.match(r'^\s*[\*\-\+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
            return None  # Will be handled by handle_lists

        # Paragraph
        if line.strip() and not self.is_table_line(line):
            return f'<p>{self.convert_inline(line)}</p>'

        return line

    def convert_header(self, line):
        """Convert markdown header to HTML with ID generation."""
        match = re.match(r'^(#{1,6})\s+(.+)', line)
        if match:
            level = len(match.group(1))
            content = match.group(2)

            # Generate ID from heading text
            heading_id = self.generate_heading_id(content)

            return f'<h{level} id="{heading_id}">{self.convert_inline(content)}</h{level}>'
        return line

    def generate_heading_id(self, text):
        """Generate a URL-friendly ID from heading text."""
        # Remove any existing HTML tags for ID generation
        import re
        clean_text = re.sub(r'<[^>]+>', '', text)

        # Convert to lowercase and replace spaces with hyphens
        heading_id = clean_text.lower()
        heading_id = re.sub(r'[^\w\s-]', '', heading_id)  # Remove special characters
        heading_id = re.sub(r'\s+', '-', heading_id)      # Replace spaces with hyphens
        heading_id = re.sub(r'-+', '-', heading_id)       # Replace multiple hyphens with single
        heading_id = heading_id.strip('-')                # Remove leading/trailing hyphens

        # Ensure it starts with a letter
        if not heading_id or not re.match(r'^[a-z]', heading_id):
            heading_id = 'heading-' + heading_id if heading_id else 'heading'

        # Handle duplicates by adding a counter
        original_id = heading_id
        counter = 1
        while heading_id in self.used_ids:
            heading_id = f"{original_id}-{counter}"
            counter += 1

        # Add to used IDs set
        self.used_ids.add(heading_id)

        return heading_id

    def convert_inline(self, text):
        """Convert inline markdown elements to HTML."""
        # Handle images first, before any other processing
        text = self.convert_images(text)

        # Process text formatting while preserving image tags
        text = self.process_formatting_with_images(text)

        # Links [text](url) - process after image handling
        text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)

        return text

    def process_formatting_with_images(self, text):
        """Process text formatting while preserving image tag content and code blocks."""
        # Store image tags to protect them from formatting
        image_placeholders = {}
        code_placeholders = {}
        image_counter = 0
        code_counter = 0

        def store_image_tag(match):
            nonlocal image_counter
            placeholder = f'IMGPLACEHOLDER{image_counter}IMGPLACEHOLDER'
            image_placeholders[placeholder] = match.group(0)
            image_counter += 1
            return placeholder

        def store_code_block(code_html):
            nonlocal code_counter
            placeholder = f'CODEPLACEHOLDER{code_counter}CODEPLACEHOLDER'
            code_placeholders[placeholder] = code_html
            code_counter += 1
            return placeholder

        # Temporarily replace image tags
        text = re.sub(r'<img[^>]*>', store_image_tag, text)

        # First convert inline code and store it to protect from formatting
        def process_code_match(match):
            code_content = self.escape_html(match.group(1))
            return store_code_block(f'<code>{code_content}</code>')

        text = re.sub(r'`([^`]+)`', process_code_match, text)

        # Now safely apply text formatting (without HTML escaping for placeholders)
        # First escape HTML but preserve our placeholders
        escaped_text = ""
        parts = text.split('IMGPLACEHOLDER')

        for i, part in enumerate(parts):
            if i % 2 == 0:  # Regular text parts
                # Apply HTML escaping and formatting to regular text
                part = self.escape_html_selective(part)

                # Bold (** or __)
                part = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', part)
                part = re.sub(r'__(.+?)__', r'<strong>\1</strong>', part)

                # Italic (* or _) - now safe from image paths and code blocks
                part = re.sub(r'\*(.+?)\*', r'<em>\1</em>', part)
                part = re.sub(r'_(.+?)_', r'<em>\1</em>', part)

                escaped_text += part
            else:  # Placeholder numbers - reconstruct placeholder
                if part:  # Only if there's a number
                    escaped_text += f'IMGPLACEHOLDER{part}IMGPLACEHOLDER'

        text = escaped_text

        # Restore image tags
        for placeholder, image_tag in image_placeholders.items():
            text = text.replace(placeholder, image_tag)

        # Restore code blocks
        for placeholder, code_block in code_placeholders.items():
            text = text.replace(placeholder, code_block)

        return text

    def convert_images(self, text):
        """Convert image markdown to HTML with proper path resolution."""
        def replace_image(match):
            alt_text = match.group(1) or ''
            image_path = match.group(2)

            # Fix path resolution for user_guide subdirectory
            if image_path.startswith('images/'):
                image_path = '../' + image_path

            return f'<img src="{image_path}" alt="{alt_text}" class="img-responsive guide-image">'

        return re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', replace_image, text)

    def escape_html_selective(self, text):
        """Escape HTML special characters but preserve placeholders."""
        # Simple HTML escaping - placeholders will be handled separately
        text = (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))

        return text

    def handle_lists(self, converted_line, original_line):
        """Handle list items and manage list stack."""
        # Check for unordered list
        ul_match = re.match(r'^(\s*)[\*\-\+]\s+(.+)', original_line)
        # Check for ordered list
        ol_match = re.match(r'^(\s*)\d+\.\s+(.+)', original_line)

        if ul_match:
            indent_level = len(ul_match.group(1)) // 2
            content = ul_match.group(2)
            return self.manage_list_stack('ul', indent_level, content)
        elif ol_match:
            indent_level = len(ol_match.group(1)) // 2
            content = ol_match.group(2)
            return self.manage_list_stack('ol', indent_level, content)
        else:
            # Not a list item, close all lists if any are open
            result = []
            while self.list_stack:
                tag = self.list_stack.pop()
                result.append(f'</{tag}>')
            if result:
                return '\n'.join(result) + '\n' + (converted_line or '')
            return converted_line

    def manage_list_stack(self, list_type, indent_level, content):
        """Manage nested lists."""
        current_level = len(self.list_stack)
        result = []

        # Close lists if we're at a lower indent level
        while current_level > indent_level + 1:
            tag = self.list_stack.pop()
            result.append(f'</{tag}>')
            current_level -= 1

        # Open new list if needed
        if current_level <= indent_level:
            self.list_stack.append(list_type)
            result.append(f'<{list_type}>')

        # Add list item
        result.append(f'<li>{self.convert_inline(content)}</li>')

        return '\n'.join(result)

    def is_table_line(self, line):
        """Check if a line is part of a table."""
        return '|' in line and line.strip().startswith('|')

    def convert_table_row(self, line):
        """Convert a table row to HTML."""
        # Remove leading and trailing pipes
        line = line.strip().strip('|')
        cells = [cell.strip() for cell in line.split('|')]

        # Check if it's a separator line
        if all(re.match(r'^[\-:]+$', cell) for cell in cells):
            return ''  # Skip separator lines

        # Determine if it's a header (simplified: first row is header)
        tag = 'th' if not self.in_table else 'td'

        row_html = '<tr>'
        for cell in cells:
            # Convert <br> tags to actual line breaks in table cells
            cell_content = cell.replace('<br>', '\n')
            # Convert the cell content and then replace newlines with <br> for HTML rendering
            converted_cell = self.convert_inline(cell_content)
            # Replace actual line breaks with HTML line breaks for proper display
            converted_cell = converted_cell.replace('\n', '<br>')
            row_html += f'<{tag}>{converted_cell}</{tag}>'
        row_html += '</tr>'

        return row_html


def create_coming_soon_template(title="Document", relative_path=""):
    """
    Create a "Coming Soon" template for disabled guides.

    Args:
        title: The title for the HTML document
        relative_path: The relative path from the HTML file to the root directory

    Returns:
        Complete HTML document as string
    """
    # Calculate the path prefix based on the depth of the file
    path_depth = relative_path.count('/') if relative_path else 0
    path_prefix = '../' * path_depth if path_depth > 0 else ''

    coming_soon_content = f"""<div class="text-center" style="padding: 60px 0;">
        <i class="icon-clock" style="font-size: 72px; color: #0077be; margin-bottom: 30px;"></i>
        <h1 style="margin-bottom: 20px;">Coming Soon</h1>
        <p style="font-size: 18px; color: #666; margin-bottom: 30px;">
            The {title} user guide is currently under development and will be available soon.
        </p>
        <p style="margin-bottom: 40px;">
            In the meantime, please explore our other available guides or check back later for updates.
        </p>
        <a href="{path_prefix}documentation.html" class="btn btn-primary">
            <i class="icon-arrow-left"></i> Back to Documentation
        </a>
    </div>"""

    return create_html_template(coming_soon_content, title, relative_path)


def create_html_template(content, title="Document", relative_path=""):
    """
    Wrap the converted markdown content in the website's HTML template.

    Args:
        content: The HTML content converted from markdown
        title: The title for the HTML document
        relative_path: The relative path from the HTML file to the root directory

    Returns:
        Complete HTML document as string
    """
    # Calculate the path prefix based on the depth of the file
    path_depth = relative_path.count('/') if relative_path else 0
    path_prefix = '../' * path_depth if path_depth > 0 else ''

    html_template = f"""<!DOCTYPE HTML>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>{title} - Eclipse Free BIRD Tools</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="{title} - Eclipse Free BIRD Tools Documentation" />
	<meta name="keywords" content="Eclipse Free BIRD Tools, Documentation, {title}" />
	<meta name="author" content="Eclipse Free BIRD Tools" />

	<!-- Facebook and Twitter integration -->
	<meta property="og:title" content="{title} - Eclipse Free BIRD Tools"/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content="Eclipse Free BIRD Tools"/>
	<meta property="og:description" content="{title} documentation for Eclipse Free BIRD Tools"/>
	<meta name="twitter:title" content="{title} - Eclipse Free BIRD Tools" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />

	<link href="https://fonts.googleapis.com/css?family=Raleway:100,300,400,700" rel="stylesheet">

	<!-- Animate.css -->
	<link rel="stylesheet" href="{path_prefix}css/animate.css">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="{path_prefix}css/icomoon.css">
	<!-- Themify Icons-->
	<link rel="stylesheet" href="{path_prefix}css/themify-icons.css">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="{path_prefix}css/bootstrap.css">
	<!-- Magnific Popup -->
	<link rel="stylesheet" href="{path_prefix}css/magnific-popup.css">
	<!-- Owl Carousel  -->
	<link rel="stylesheet" href="{path_prefix}css/owl.carousel.min.css">
	<link rel="stylesheet" href="{path_prefix}css/owl.theme.default.min.css">
	<!-- Theme style  -->
	<link rel="stylesheet" href="{path_prefix}css/style.css">

	<!-- Modernizr JS -->
	<script src="{path_prefix}js/modernizr-2.6.2.min.js"></script>
	<!-- Page Allowlist Check -->
	<script src="{path_prefix}js/allowlist.js"></script>
	<!-- FOR IE9 below -->
	<!--[if lt IE 9]>
	<script src="{path_prefix}js/respond.min.js"></script>
	<![endif]-->

	<style>
		/* Clean, modern documentation styles */
		.doc-content {{
			padding: 60px 0;
			min-height: 600px;
			background: white;
		}}

		.content-wrapper {{
			max-width: 900px;
			margin: 0 auto;
			padding: 0 40px;
		}}

		/* Typography */
		.doc-content h1 {{
			color: #192a45;
			font-size: 2.5rem;
			font-weight: 700;
			border-bottom: 3px solid #17B794;
			padding-bottom: 15px;
			margin-bottom: 35px;
		}}

		.doc-content h2 {{
			color: #2c3e50;
			font-size: 1.8rem;
			font-weight: 600;
			margin-top: 45px;
			margin-bottom: 25px;
			padding-top: 20px;
		}}

		.doc-content h3 {{
			color: #34495e;
			font-size: 1.4rem;
			font-weight: 600;
			margin-top: 35px;
			margin-bottom: 20px;
		}}

		.doc-content p {{
			font-size: 16px;
			line-height: 1.8;
			color: #4a5568;
			margin: 20px 0;
		}}

		/* Code blocks */
		.doc-content pre {{
			background: #f7fafc;
			border: 1px solid #e2e8f0;
			border-left: 4px solid #17B794;
			padding: 20px;
			border-radius: 8px;
			overflow-x: auto;
			margin: 25px 0;
			font-size: 14px;
		}}

		.doc-content code {{
			background: #f7fafc;
			padding: 3px 6px;
			border-radius: 4px;
			font-family: 'Monaco', 'Courier New', monospace;
			font-size: 0.9em;
			color: #e53e3e;
		}}

		.doc-content pre code {{
			background: transparent;
			padding: 0;
			color: #2d3748;
		}}

		/* Blockquotes */
		.doc-content blockquote {{
			background: #f0fdf4;
			border-left: 4px solid #17B794;
			margin: 25px 0;
			padding: 20px 25px;
			color: #2d3748;
			font-style: italic;
			border-radius: 0 8px 8px 0;
		}}

		/* Lists */
		.doc-content ul, .doc-content ol {{
			margin: 20px 0;
			padding-left: 35px;
			color: #4a5568;
		}}

		.doc-content li {{
			margin: 10px 0;
			line-height: 1.7;
		}}

		/* Images */
		.doc-content img {{
			margin: 30px auto;
			display: block;
		}}

		.doc-content .guide-image {{
			max-width: 100%;
			height: auto;
			border: 2px solid #e2e8f0;
			border-radius: 12px;
			box-shadow: 0 4px 12px rgba(0,0,0,0.08);
			margin: 35px auto;
			display: block;
			transition: all 0.3s ease;
		}}

		.doc-content .guide-image:hover {{
			transform: translateY(-2px);
			box-shadow: 0 8px 24px rgba(0,0,0,0.12);
			border-color: #008793;
		}}

		/* Links */
		.doc-content a {{
			color: #17B794;
			text-decoration: none;
			font-weight: 500;
			transition: all 0.2s ease;
			border-bottom: 1px solid transparent;
		}}

		.doc-content a:hover {{
			color: #0e7c61;
			border-bottom-color: #17B794;
		}}

		/* Tables */
		.doc-content table {{
			width: 100%;
			margin: 30px 0;
			border-collapse: collapse;
			border: 1px solid #e2e8f0;
			border-radius: 8px;
			overflow: hidden;
		}}

		.doc-content table th {{
			background: #f7fafc;
			padding: 12px 15px;
			text-align: left;
			font-weight: 600;
			color: #2d3748;
			border-bottom: 2px solid #e2e8f0;
		}}

		.doc-content table td {{
			padding: 12px 15px;
			border-bottom: 1px solid #e2e8f0;
		}}

		.doc-content table tr:last-child td {{
			border-bottom: none;
		}}

		/* Horizontal rule */
		.doc-content hr {{
			border: none;
			height: 2px;
			background: linear-gradient(to right, transparent, #e2e8f0, transparent);
			margin: 50px 0;
		}}

		/* Responsive adjustments */
		@media (max-width: 768px) {{
			.content-wrapper {{
				padding: 0 20px;
			}}

			.doc-content h1 {{
				font-size: 2rem;
			}}

			.doc-content h2 {{
				font-size: 1.5rem;
			}}

			.doc-content h3 {{
				font-size: 1.2rem;
			}}
		}}
	</style>
</head>
<body>

<div class="gtco-loader"></div>

<div id="page">

	<!-- Navigation Include -->
	<div w3-include-html="{path_prefix}navbar.html"></div>

	<header class="hero-section">
		<div class="gtco-container">
			<div class="row">
				<div class="col-md-12 text-center">
					<h1>{title}</h1>
					<h2>Eclipse Free BIRD Tools Documentation</h2>
				</div>
			</div>
		</div>
	</header>

	<!-- Dynamic Sidebar will be inserted here by JavaScript -->

	<!-- Main Content -->
	<section class="main doc-content ">
  		<div class="content-wrapper">
 			{content}
  		</div>
	</section>

	<!-- Footer Include -->
	<div w3-include-html="{path_prefix}footer.html"></div>

</div>

<!-- jQuery -->
<script src="{path_prefix}js/jquery.min.js"></script>
<!-- jQuery Easing -->
<script src="{path_prefix}js/jquery.easing.1.3.js"></script>
<!-- Bootstrap -->
<script src="{path_prefix}js/bootstrap.min.js"></script>
<!-- Waypoints -->
<script src="{path_prefix}js/jquery.waypoints.min.js"></script>
<!-- Carousel -->
<script src="{path_prefix}js/owl.carousel.min.js"></script>
<!-- Magnific Popup -->
<script src="{path_prefix}js/jquery.magnific-popup.min.js"></script>
<script src="{path_prefix}js/magnific-popup-options.js"></script>
<!-- Main -->
<script src="{path_prefix}js/main.js"></script>
<!-- W3 Include -->
<script src="{path_prefix}js/w3-include.js"></script>
<!-- Dynamic Sidebar -->
<script src="{path_prefix}js/dynamic-sidebar.js"></script>

</body>
</html>"""
    return html_template


def extract_description_from_markdown(markdown_content):
    """
    Extract the first paragraph from markdown content as description.

    Args:
        markdown_content: The markdown content as string

    Returns:
        Description string or empty string if not found
    """
    lines = markdown_content.split('\n')
    description = ""

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('-') and not line.startswith('*'):
            # Remove markdown formatting for description
            description = re.sub(r'\*\*(.+?)\*\*', r'\1', line)  # Bold
            description = re.sub(r'\*(.+?)\*', r'\1', description)  # Italic
            description = re.sub(r'`([^`]+)`', r'\1', description)  # Code
            description = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', description)  # Links
            break

    return description


def convert_markdown_to_html(markdown_file_path, output_file_path):
    """
    Convert a single markdown file to HTML.

    Args:
        markdown_file_path: Path to the input markdown file
        output_file_path: Path where the HTML file should be saved

    Returns:
        Dictionary with guide metadata if successful, None otherwise
    """
    try:
        # Get the slug from the filename
        slug = Path(markdown_file_path).stem

        # Get the title from the filename
        title = slug.replace('_', ' ').replace('-', ' ').title()

        # Calculate relative path for includes
        relative_path = str(Path(output_file_path).relative_to(Path('.')))

        # Check if this guide is disabled (always override with "Coming Soon" page)
        if slug in DISABLED_GUIDES:
            print(f"        Guide '{slug}' is disabled - creating 'Coming Soon' page")

            # Create a "Coming Soon" page instead
            full_html = create_coming_soon_template(title, relative_path)

            # Create output directory if it doesn't exist
            output_dir = Path(output_file_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)

            # Write the HTML file (this will overwrite any existing content)
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(full_html)

            # Return metadata for index generation (marked as disabled)
            return {
                'title': title,
                'description': 'This guide is currently under development and will be available soon.',
                'filename': Path(output_file_path).name,
                'path': str(Path(output_file_path).relative_to(Path('.'))),
                'last_modified': datetime.now().isoformat(),
                'slug': slug,
                'disabled': True,
                'status': 'coming_soon'
            }

        # Normal processing for enabled guides
        # Read the markdown file
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Convert markdown to HTML using our custom converter
        converter = MarkdownToHTMLConverter()
        html_content = converter.convert(markdown_content)

        # Extract description from markdown content
        description = extract_description_from_markdown(markdown_content)

        # Wrap in HTML template with proper path prefixes
        full_html = create_html_template(html_content, title, relative_path)

        # Create output directory if it doesn't exist
        output_dir = Path(output_file_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Write the HTML file
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

        # Return metadata for index generation
        return {
            'title': title,
            'description': description,
            'filename': Path(output_file_path).name,
            'path': str(Path(output_file_path).relative_to(Path('.'))),
            'last_modified': datetime.now().isoformat(),
            'slug': slug,
            'disabled': False,
            'status': 'available'
        }

    except Exception as e:
        print(f"Error converting {markdown_file_path}: {str(e)}")
        return None


def generate_guide_index(guides_metadata, output_dir="user-guide"):
    """
    Generate an index.json file with metadata about all guides.

    Args:
        guides_metadata: List of guide metadata dictionaries
        output_dir: Directory where to save the index.json file
    """
    index_data = {
        'generated_at': datetime.now().isoformat(),
        'total_guides': len(guides_metadata),
        'guides': guides_metadata
    }

    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Write index.json
    index_file = Path(output_dir) / "index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print(f"Generated guide index: {index_file}")


def process_markdown_directory(source_dir="markdown_content", base_output_dir="."):
    """
    Process all markdown files in the source directory and convert them to HTML.

    Args:
        source_dir: The directory containing markdown files
        base_output_dir: The base directory for output files
    """
    source_path = Path(source_dir)
    base_output_path = Path(base_output_dir)

    if not source_path.exists():
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Find all markdown files
    markdown_files = list(source_path.rglob("*.md"))

    if not markdown_files:
        print(f"No markdown files found in '{source_dir}'")
        print("Creating a sample markdown file for demonstration...")

        # Create a sample structure for demonstration
        sample_dir = Path("markdown_content/user-guide")
        sample_dir.mkdir(parents=True, exist_ok=True)

        # Create a sample markdown file
        sample_file = sample_dir / "getting_started.md"
        sample_content = """# Getting Started with Eclipse Free BIRD Tools

## Introduction

Welcome to the Eclipse Free BIRD Tools user guide. This comprehensive guide will help you get started with the Eclipse Free BIRD Tools platform, a powerful solution for regulatory reporting and data transformation.

## Prerequisites

Before you begin, ensure you have the following:

- **Java 11 or higher** installed on your system
- **Git** for version control
- At least **4GB of RAM** (8GB recommended)
- **500MB of free disk space**

## Installation

### Quick Installation

The fastest way to get started is using our installation scripts:

#### For Windows Users

```bash
git clone https://github.com/eclipse-efbt/efbt.git
cd efbt
windows_startup.bat
```

#### For Linux and macOS Users

```bash
git clone https://github.com/eclipse-efbt/efbt.git
cd efbt
chmod +x linux_startup.sh
./linux_startup.sh
```

### Manual Installation

If you prefer manual installation, follow these steps:

1. Clone the repository
2. Configure your environment variables
3. Install dependencies
4. Run the application

## Core Concepts

### Data Models

Eclipse Free BIRD Tools uses a sophisticated data modeling approach that includes:

- **Input Data Models**: Define the structure of incoming data
- **Transformation Rules**: Specify how data should be processed
- **Output Models**: Define the target format for regulatory reports

### Transformations

Transformations in Eclipse Free BIRD Tools follow these principles:

| Principle | Description |
|-----------|-------------|
| **Traceability** | Every transformation can be traced back to its source |
| **Validation** | Built-in validation ensures data integrity |
| **Reusability** | Transformation components can be reused across projects |
| **Performance** | Optimized for handling large datasets |

## Working with Projects

### Creating a New Project

To create a new project:

1. Open Eclipse Free BIRD Tools
2. Select **File > New > Project**
3. Choose **BIRD Project** from the wizard
4. Follow the setup instructions

### Project Structure

A typical project contains:

- `models/` - Data model definitions
- `transformations/` - Transformation rules
- `tests/` - Test cases and validation rules
- `output/` - Generated reports

## Best Practices

> **Note**: Following these best practices will help you get the most out of Eclipse Free BIRD Tools.

### Version Control

- Always use version control for your projects
- Commit changes frequently with meaningful messages
- Use branching for experimental features

### Testing

- Write tests for all transformations
- Validate data at each transformation step
- Use sample data for development

### Performance Optimization

1. **Batch Processing**: Process data in batches for better performance
2. **Caching**: Enable caching for frequently accessed data
3. **Parallel Processing**: Utilize multi-threading where possible

## Troubleshooting

### Common Issues

**Issue: Application won't start**
- Check Java version: `java -version`
- Ensure all dependencies are installed
- Check log files in `logs/` directory

**Issue: Transformation fails**
- Validate input data format
- Check transformation rules syntax
- Review error messages in console

## Next Steps

Now that you have Eclipse Free BIRD Tools installed and understand the basics:

- Explore the [API Reference](api_reference.html)
- Review [Sample Projects](samples.html)
- Join our [Community Forum](https://forum.eclipse.org/efbt)

---

*For more information, visit the [Eclipse Free BIRD Tools website](https://eclipse.org/efbt)*
"""
        with open(sample_file, 'w') as f:
            f.write(sample_content)
        print(f"Created sample file: {sample_file}")

        # Re-scan for markdown files
        markdown_files = list(source_path.rglob("*.md"))

    print(f"Found {len(markdown_files)} markdown file(s) to convert.")
    print("-" * 50)

    successful = 0
    failed = 0
    guides_metadata = []

    for md_file in markdown_files:
        # Calculate the relative path from source_dir
        relative_path = md_file.relative_to(source_path)

        # Create the output path (remove markdown_content prefix)
        output_path = base_output_path / relative_path.with_suffix('.html')

        print(f"Converting: {md_file}")
        print(f"        to: {output_path}")

        guide_metadata = convert_markdown_to_html(md_file, output_path)
        if guide_metadata:
            successful += 1
            guides_metadata.append(guide_metadata)
            print("        ✓ Success")
        else:
            failed += 1
            print("        ✗ Failed")
        print()

    # Generate index.json file
    if guides_metadata:
        generate_guide_index(guides_metadata)

    print("-" * 50)
    print(f"Conversion complete: {successful} successful, {failed} failed")


def disable_guide(guide_slug):
    """
    Disable a guide by adding it to the DISABLED_GUIDES list.

    Args:
        guide_slug: The slug of the guide to disable (e.g., 'dataset_transformation')
    """
    if guide_slug not in DISABLED_GUIDES:
        print(f"Disabling guide: {guide_slug}")
        # Note: This would require modifying the source code or using a config file
        print(f"Add '{guide_slug}' to the DISABLED_GUIDES list in this script and re-run.")
    else:
        print(f"Guide '{guide_slug}' is already disabled.")


def enable_guide(guide_slug):
    """
    Enable a guide by removing it from the DISABLED_GUIDES list.

    Args:
        guide_slug: The slug of the guide to enable (e.g., 'dataset_transformation')
    """
    if guide_slug in DISABLED_GUIDES:
        print(f"Enabling guide: {guide_slug}")
        # Note: This would require modifying the source code or using a config file
        print(f"Remove '{guide_slug}' from the DISABLED_GUIDES list in this script and re-run.")
    else:
        print(f"Guide '{guide_slug}' is already enabled.")


def main():
    """Main function to run the converter."""
    print("Markdown to HTML Converter (Website Styled)")
    print("=" * 50)

    # Show current disabled guides
    if DISABLED_GUIDES:
        print(f"Currently disabled guides: {', '.join(DISABLED_GUIDES)}")
        print("-" * 50)

    # Check if markdown_content directory exists
    if not Path("markdown_content").exists():
        print("Creating 'markdown_content' directory...")
        Path("markdown_content").mkdir(exist_ok=True)
        print("Please place your markdown files in the 'markdown_content' directory.")

    # Process the markdown files
    process_markdown_directory()

    # Show usage instructions
    print()
    print("=" * 50)
    print("GUIDE MANAGEMENT:")
    print("To disable a guide: Add the guide slug to DISABLED_GUIDES list at the top of this script")
    print("To enable a guide: Remove the guide slug from DISABLED_GUIDES list")
    print("Then re-run this script to regenerate all HTML files")
    print()
    print("Available guide slugs:")
    markdown_files = list(Path("markdown_content").rglob("*.md"))
    for md_file in markdown_files:
        slug = md_file.stem
        status = "DISABLED" if slug in DISABLED_GUIDES else "enabled"
        print(f"  - {slug} ({status})")
    print("=" * 50)


if __name__ == "__main__":
    main()
