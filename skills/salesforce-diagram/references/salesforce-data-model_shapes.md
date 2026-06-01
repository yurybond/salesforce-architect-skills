# Salesforce Data Model Shapes

Source template: .agents/skills/drawio-skill/assets/templates/salesforce-data_model.drawio

This document provides reusable draw.io XML building blocks for Salesforce data model diagrams.
Use placeholders like {{ID}}, {{LABEL}}, {{X}}, {{Y}}, {{W}}, {{H}}, {{SOURCE_ID}}, and {{TARGET_ID}}.

## 0. Mandatory Header Contract

For Salesforce data model/ERD generation, include the standard Salesforce header block from `references/salesforce-diagram_header.md`.

- Seed first pass from `assets/templates/salesforce-data_model.drawio`.
- Keep the header structure intact: gray header container, left title/subtitle panel, and white key/legend box in header.
- Update header content (title/subtitle and legend text) for the current domain, but do not remove header cells.

## 1. Building Blocks

### 1.1 Blue Object Block
Use for custom or included-license objects.

    <mxCell id="{{ID}}" value="{{LABEL}}" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontSize=20;fontStyle=1;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;fontColor=#003366;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry"/>
    </mxCell>

Example:

    <mxCell id="10" value="Store" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontSize=20;fontStyle=1;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;fontColor=#003366;" parent="1" vertex="1">
      <mxGeometry x="60" y="80" width="220" height="110" as="geometry"/>
    </mxCell>

### 1.2 Gray Object Block
Use for Salesforce standard objects.

    <mxCell id="{{ID}}" value="{{LABEL}}" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#e3e4e6;strokeColor=#2b2b2f;strokeWidth=3;fontSize=20;fontStyle=1;fontColor=#2d2e33;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry"/>
    </mxCell>

Example:

    <mxCell id="13" value="Account" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#e3e4e6;strokeColor=#2b2b2f;strokeWidth=3;fontSize=20;fontStyle=1;fontColor=#2d2e33;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;" parent="1" vertex="1">
      <mxGeometry x="60" y="425" width="220" height="110" as="geometry"/>
    </mxCell>

### 1.3 Tall Anchor Block
Use for a central aggregate object (for example, Cart).

    <mxCell id="{{ID}}" value="{{LABEL}}" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontSize=21;fontStyle=1;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;fontColor=#003366;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry"/>
    </mxCell>

Example:

    <mxCell id="11" value="Cart" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontSize=21;fontStyle=1;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;fontColor=#003366;" parent="1" vertex="1">
      <mxGeometry x="380" y="80" width="130" height="880" as="geometry"/>
    </mxCell>

### 1.4 Legend Building Blocks
Legend text:

    <mxCell id="{{ID}}" value="{{TEXT}}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=2;fontColor=#4a4a4a;fontFamily=Helvetica;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry"/>
    </mxCell>

Legend marker (blue):

    <mxCell id="{{ID}}" value="" style="rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="24" height="24" as="geometry"/>
    </mxCell>

Legend marker (gray):

    <mxCell id="{{ID}}" value="" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#e3e4e6;strokeColor=#2b2b2f;strokeWidth=2;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="24" height="24" as="geometry"/>
    </mxCell>

## 2. Connectors

### 2.1 Straight ER Connector Template

    <mxCell id="{{ID}}" value="" style="edgeStyle=straightEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;startArrow={{START_ARROW}};startFill=0;endArrow={{END_ARROW}};endFill=0;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

Example (one to many):

    <mxCell id="302" value="" style="edgeStyle=straightEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;startArrow=ERone;startFill=0;endArrow=ERzeroToMany;endFill=0;" parent="1" source="10" target="11" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

### 2.2 Orthogonal ER Connector Template
Use when straight lines overlap too much.

    <mxCell id="{{ID}}" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;startArrow={{START_ARROW}};startFill=0;endArrow={{END_ARROW}};endFill=0;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

Example:

    <mxCell id="124" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;startArrow=ERzeroToMany;startFill=0;endArrow=ERzeroToOne;endFill=0;" parent="1" source="29" target="24" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

### 2.3 Connector With Routing Points
Use explicit entry and exit points for precise layout.

    <mxCell id="{{ID}}" value="" style="edgeStyle=straightEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;startArrow={{START_ARROW}};startFill=0;endArrow={{END_ARROW}};endFill=0;exitX={{EXIT_X}};exitY={{EXIT_Y}};exitDx=0;exitDy=0;entryX={{ENTRY_X}};entryY={{ENTRY_Y}};entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

Example:

    <mxCell id="116" value="" style="edgeStyle=straightEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;startArrow=ERzeroToOne;startFill=0;endArrow=ERzeroToMany;endFill=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=0.993;exitY=0.715;exitDx=0;exitDy=0;exitPerimeter=0;" parent="1" source="11" target="26" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

## 3. Cardinality Presets

- One to many: startArrow=ERone; endArrow=ERzeroToMany
- Optional one to many: startArrow=ERzeroToOne; endArrow=ERzeroToMany
- Many to mandatory one: startArrow=ERzeroToMany; endArrow=ERmandOne
- Many to one: startArrow=ERzeroToMany; endArrow=ERone
- One to one: startArrow=ERone; endArrow=ERone
- One to many mandatory: startArrow=ERone; endArrow=ERmany

## 4. Minimal Skeleton Example

    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <mxCell id="10" value="Store" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontSize=20;fontStyle=1;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;fontColor=#003366;" parent="1" vertex="1">
      <mxGeometry x="60" y="80" width="220" height="110" as="geometry"/>
    </mxCell>

    <mxCell id="11" value="Cart" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontSize=21;fontStyle=1;fontFamily=Helvetica;align=left;verticalAlign=top;spacingLeft=12;spacingTop=10;fontColor=#003366;" parent="1" vertex="1">
      <mxGeometry x="380" y="80" width="130" height="880" as="geometry"/>
    </mxCell>

    <mxCell id="302" value="" style="edgeStyle=straightEdgeStyle;rounded=0;html=1;strokeWidth=3;strokeColor=#6a6d73;startSize=18;endSize=18;startArrow=ERone;startFill=0;endArrow=ERzeroToMany;endFill=0;" parent="1" source="10" target="11" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

## 5. First-Pass Generation Checklist

Apply this checklist for Salesforce ERD generation to avoid common first-attempt defects.

### 5.0 Header Contract

- Header block is present and follows `references/salesforce-diagram_header.md`.
- Legend/key remains inside the header container, not floating in root.
- Header and legend are fully visible within page bounds.

### 5.1 Object Classification

- Standard object: API name does not end with `__c` -> use Gray Object Block.
- Custom/licensed object: API name ends with `__c` -> use Blue Object Block.

### 5.2 Object Label Contract

- Label format: `Label [ApiName]`
- Do not include relationship counters in labels.
- Do not include source metadata paths in labels.

### 5.3 Relationship Mapping Contract

- MasterDetail field -> `startArrow=ERone;endArrow=ERzeroToMany;`
- Lookup field (optional parent) -> `startArrow=ERzeroToOne;endArrow=ERzeroToMany;`
- Use `edgeStyle=orthogonalEdgeStyle` by default for better readability in dense models.

### 5.4 Typography Contract

- Object block font must be Helvetica.
- Object block title font should be bold and size 20.

## 6. Common Reasons First Attempt Is Incorrect

- Generic connector arrows (`endArrow=block`) used instead of ER arrows.
- No object type classification, causing standard objects to render as custom-style blocks.
- Label text includes non-domain metadata (relationship count, file paths).
- Ad-hoc font choices and font sizes instead of Salesforce data-model presets.
