#!/usr/bin/env python3
"""
Review Logic Implementation for Code Review Assistant
This module handles processing code files and applying review templates.
"""

import os
import re
import sys
import argparse
from typing import Dict, List, Optional, Set, Tuple


class ReviewTemplate:
    """Class representing a code review template."""
    
    def __init__(self, template_path: str):
        """Initialize template from a file path."""
        self.path = template_path
        self.name = os.path.basename(template_path).replace('.md', '')
        self.content = ''
        self.sections = {}
        self._load_template()
        
    def _load_template(self) -> None:
        """Load the template content from file."""
        try:
            with open(self.path, 'r') as f:
                self.content = f.read()
                self._parse_sections()
        except FileNotFoundError:
            print(f"Error: Template file {self.path} not found.")
            sys.exit(1)
            
    def _parse_sections(self) -> None:
        """Parse the template into sections for structured access."""
        current_section = None
        section_content = []
        
        for line in self.content.split('\n'):
            if line.startswith('## '):
                if current_section:
                    self.sections[current_section] = '\n'.join(section_content)
                current_section = line[3:].strip()
                section_content = []
            else:
                section_content.append(line)
                
        if current_section:
            self.sections[current_section] = '\n'.join(section_content)
            
    def get_section(self, section_name: str) -> str:
        """Get content of a specific section."""
        return self.sections.get(section_name, '')
    
    def apply_to_code(self, code_content: str) -> str:
        """Apply the template to analyze code content."""
        review_result = f"# Code Review: {self.name.title()} Review\n\n"
        review_result += f"## Code Overview\n{self._generate_code_summary(code_content)}\n\n"
        
        for section, content in self.sections.items():
            review_result += f"## {section}\n{content}\n\n"
            
        return review_result
        
    def _generate_code_summary(self, code_content: str) -> str:
        """Generate a summary of the code."""
        lines = code_content.split('\n')
        loc = len(lines)
        functions = len(re.findall(r'def\s+\w+\s*\(', code_content))
        classes = len(re.findall(r'class\s+\w+\s*(\(|:)', code_content))
        
        summary = f"- Lines of code: {loc}\n"
        summary += f"- Functions: {functions}\n"
        summary += f"- Classes: {classes}\n"
        
        return summary


class CodeReviewer:
    """Main class for handling code reviews."""
    
    def __init__(self, templates_dir: str = "./review_templates"):
        """Initialize with path to templates directory."""
        self.templates_dir = templates_dir
        self.templates = self._load_all_templates()
        
    def _load_all_templates(self) -> Dict[str, ReviewTemplate]:
        """Load all available templates."""
        templates = {}
        try:
            for filename in os.listdir(self.templates_dir):
                if filename.endswith('.md'):
                    template_path = os.path.join(self.templates_dir, filename)
                    template = ReviewTemplate(template_path)
                    templates[template.name] = template
        except FileNotFoundError:
            print(f"Error: Templates directory {self.templates_dir} not found.")
            sys.exit(1)
            
        return templates
    
    def get_available_templates(self) -> List[str]:
        """Get list of available template names."""
        return list(self.templates.keys())
    
    def review_code(self, code_path: str, template_name: str) -> str:
        """Review code using specified template."""
        # Validate template exists
        if template_name not in self.templates:
            available = ', '.join(self.get_available_templates())
            print(f"Error: Template '{template_name}' not found. Available templates: {available}")
            sys.exit(1)
            
        # Load code file
        try:
            with open(code_path, 'r') as f:
                code_content = f.read()
        except FileNotFoundError:
            print(f"Error: Code file {code_path} not found.")
            sys.exit(1)
            
        # Apply template to code
        template = self.templates[template_name]
        return template.apply_to_code(code_content)
        
    def batch_review(self, code_path: str) -> Dict[str, str]:
        """Run all templates against the code."""
        results = {}
        for template_name in self.templates:
            results[template_name] = self.review_code(code_path, template_name)
        return results


def main():
    """Main function for CLI usage."""
    parser = argparse.ArgumentParser(description="Code Review Assistant")
    parser.add_argument("code_file", help="Path to code file to review")
    parser.add_argument("--template", "-t", help="Template to use for review")
    parser.add_argument("--list-templates", "-l", action="store_true", help="List available templates")
    parser.add_argument("--templates-dir", "-d", default="./review_templates", help="Directory with review templates")
    parser.add_argument("--output", "-o", help="Output file for review results")
    
    args = parser.parse_args()
    
    reviewer = CodeReviewer(args.templates_dir)
    
    if args.list_templates:
        templates = reviewer.get_available_templates()
        print("Available templates:")
        for template in templates:
            print(f"- {template}")
        return
        
    # If template specified, use that one, otherwise use all
    if args.template:
        result = reviewer.review_code(args.code_file, args.template)
        results = {args.template: result}
    else:
        results = reviewer.batch_review(args.code_file)
        
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            for template_name, review in results.items():
                f.write(f"{'=' * 80}\n")
                f.write(f"REVIEW USING {template_name.upper()} TEMPLATE\n")
                f.write(f"{'=' * 80}\n\n")
                f.write(review)
                f.write("\n\n")
    else:
        for template_name, review in results.items():
            print(f"{'=' * 80}")
            print(f"REVIEW USING {template_name.upper()} TEMPLATE")
            print(f"{'=' * 80}\n")
            print(review)
            print("\n")


if __name__ == "__main__":
    main()