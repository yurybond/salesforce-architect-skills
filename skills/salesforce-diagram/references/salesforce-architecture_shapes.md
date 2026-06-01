# Salesforce Architecture Shapes

Source template: `.agents/skills/drawio-skill/assets/templates/salesforce-system_overview.drawio`

This document provides reusable draw.io XML building blocks for Salesforce architecture diagrams.
Use placeholders like {{ID}}, {{PARENT_ID}}, {{LABEL}}, {{X}}, {{Y}}, {{W}}, {{H}}, {{SOURCE_ID}}, and {{TARGET_ID}}.

## 1. Header

### 1.1 Header Container (top gray strip)
Use as the full header background.

    <mxCell id="{{ID}}" parent="1" style="strokeColor=#E6E6E6;fillColor=#d9d9d9;fontSize=16;" value="" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry" />
    </mxCell>

### 1.2 Header Intro Panel (left delay shape)
Use as the title/description host.

    <mxCell id="{{ID}}" parent="{{HEADER_ID}}" style="shape=delay;whiteSpace=wrap;html=1;strokeColor=none;resizeHeight=1;part=1;fontSize=16;" value="" vertex="1">
      <mxGeometry width="350" height="160" relative="1" as="geometry" />
    </mxCell>

### 1.3 Header Rich Text
Use for layer title and subtitle.

    <mxCell id="{{ID}}" parent="{{INTRO_PANEL_ID}}" style="text;html=1;strokeColor=none;fillColor=none;spacing=5;spacingTop=-20;whiteSpace=wrap;overflow=hidden;rounded=0;part=1;fontSize=16;" value="&lt;h3&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;{{TITLE}}&lt;/font&gt;&lt;/h3&gt;&lt;p&gt;&lt;font style=&quot;font-size: 9px;&quot;&gt;{{SUBTITLE}}&lt;/font&gt;&lt;/p&gt;" vertex="1">
      <mxGeometry width="320" height="110" relative="1" as="geometry">
        <mxPoint x="20" y="40" as="offset" />
      </mxGeometry>
    </mxCell>

## 2. Header Legend

### 2.1 Legend Box
Use as legend container in the header.

    <mxCell id="{{ID}}" parent="{{HEADER_ID}}" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=none;verticalAlign=top;align=left;spacingLeft=10;fontSize=11;part=1;" value="Key" vertex="1">
      <mxGeometry x="1" width="{{W}}" height="{{H}}" relative="1" as="geometry">
        <mxPoint x="{{OFFSET_X}}" y="{{OFFSET_Y}}" as="offset" />
      </mxGeometry>
    </mxCell>

### 2.2 Brand/Platform Mark
Use for the draw.io logo marker shown in all layer headers.

    <mxCell id="{{ID}}" parent="{{HEADER_ID}}" style="dashed=0;outlineConnect=0;html=1;align=center;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;shape=mxgraph.weblogos.drawio2;fillColor=#1A5BA3;fontSize=16;" value="" vertex="1">
      <mxGeometry x="20" y="10" width="22" height="26" as="geometry" />
    </mxCell>

### 2.3 Legend Item (icon + label)
Use for each capability in the header key.

    <mxCell id="{{ICON_ID}}" parent="{{HEADER_ID}}" style="whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#e5e5e5;part=1;fontSize=10;verticalLabelPosition=middle;shape={{ICON_SHAPE}};labelPosition=right;align=left;verticalAlign=middle;" value="{{LABEL}}" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="26" height="26" as="geometry" />
    </mxCell>

Typical icon shapes in this template include:
- `mxgraph.salesforce.web2`
- `mxgraph.salesforce.apps2`
- `mxgraph.salesforce.commerce2`
- `mxgraph.salesforce.workflow2`
- `mxgraph.salesforce.customer_3602`
- `mxgraph.salesforce.learning2`
- `mxgraph.salesforce.integration2`

## 3. Cards (blocks) with icons, title, and items

### 3.1 Standard Card Container
Most reusable card shell across layers.

    <mxCell id="{{ID}}" parent="{{PARENT_ID}}" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#B3B3B3;arcSize=20;absoluteArcSize=1;fontSize=16;" value="" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry" />
    </mxCell>

### 3.2 Channel/Pill Card Variant
Same geometry pattern, but no border and gray fill.

    <mxCell id="{{ID}}" parent="{{PARENT_ID}}" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=none;arcSize=20;absoluteArcSize=1;fontSize=16;fillColor=#D9D9D9;" value="" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="200" height="70" as="geometry" />
    </mxCell>

### 3.3 Card Leading Icon
Primary icon in card header area.

    <mxCell id="{{ID}}" parent="{{CARD_ID}}" style="whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#e5e5e5;part=1;fontSize=16;verticalLabelPosition=bottom;shape={{ICON_SHAPE}};" value="" vertex="1">
      <mxGeometry width="46" height="46" relative="1" as="geometry">
        <mxPoint x="15" y="10" as="offset" />
      </mxGeometry>
    </mxCell>

### 3.4 Card Title Strip
Bold top strip label used in nearly all cards.

    <mxCell id="{{ID}}" parent="{{CARD_ID}}" style="shape=partialRectangle;whiteSpace=wrap;html=1;top=0;left=0;fillColor=none;right=0;fontStyle=1;align=left;strokeColor=#B3B3B3;part=1;fontSize=16;" value="{{TITLE}}" vertex="1">
      <mxGeometry x="1" width="130" height="30" relative="1" as="geometry">
        <mxPoint x="-130" y="20" as="offset" />
      </mxGeometry>
    </mxCell>

### 3.5 Card Item Text Row
Use for textual capabilities/items under card title.

    <mxCell id="{{ID}}" parent="{{CARD_ID}}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;part=1;fontSize=13;" value="{{ITEM_TEXT}}" vertex="1">
      <mxGeometry width="130" height="24" x="70" y="{{Y}}" as="geometry" />
    </mxCell>

### 3.6 Multi-Icon Row Inside Card
Used for capability rows with several 36x36 icons.

    <mxCell id="{{ID}}" parent="{{CARD_ID}}" style="whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#e5e5e5;part=1;fontSize=13;verticalLabelPosition=middle;shape={{ICON_SHAPE}};labelPosition=right;align=left;verticalAlign=middle;" value="" vertex="1">
      <mxGeometry width="36" height="36" relative="1" as="geometry">
        <mxPoint x="{{OFFSET_X}}" y="-55" as="offset" />
      </mxGeometry>
    </mxCell>

### 3.7 Sub-Section Panel Inside Large Card
Used in Layer 2/4 as nested sections (UX, Process, System).

    <mxCell id="{{ID}}" parent="{{CARD_ID}}" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#B3B3B3;arcSize=20;absoluteArcSize=1;fontSize=16;" value="" vertex="1">
      <mxGeometry x="10" y="{{Y}}" width="200" height="{{H}}" as="geometry" />
    </mxCell>

### 3.8 Section Header in Panel

    <mxCell id="{{ID}}" parent="{{PANEL_ID}}" style="shape=partialRectangle;whiteSpace=wrap;html=1;top=0;left=0;fillColor=none;right=0;fontStyle=1;align=left;strokeColor=#B3B3B3;spacingLeft=15;part=1;resizeWidth=1;fontSize=16;" value="{{SECTION_TITLE}}" vertex="1">
      <mxGeometry width="200" height="30" relative="1" as="geometry">
        <mxPoint y="20" as="offset" />
      </mxGeometry>
    </mxCell>

### 3.9 Section Item Row in Panel

    <mxCell id="{{ID}}" parent="{{PANEL_ID}}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;spacingLeft=15;part=1;resizeWidth=1;fontSize=16;" value="{{ITEM_TEXT}}" vertex="1">
      <mxGeometry width="200" height="24" relative="1" as="geometry">
        <mxPoint y="{{OFFSET_Y}}" as="offset" />
      </mxGeometry>
    </mxCell>

### 3.10 Compact 40px Mini Card (bottom strip cards)

    <mxCell id="{{ID}}" parent="{{PARENT_ID}}" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#B3B3B3;arcSize=20;absoluteArcSize=1;fontSize=16;" value="" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="132.88888888888889" height="40" as="geometry" />
    </mxCell>

## 4. Connectors

### 4.1 Curved Structural Connector (solid, classic start arrow)
Main architecture dependency line (Layer 1).

    <mxCell id="{{ID}}" edge="1" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;startArrow=classic;startFill=1;">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>

### 4.2 Curved Integration Connector (dashed with label)
Used heavily in Layer 2 mappings.

    <mxCell id="{{ID}}" value="{{RELATION_LABEL}}" style="edgeStyle=none;shape=connector;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;labelBackgroundColor=default;strokeColor=default;align=center;verticalAlign=middle;fontFamily=Helvetica;fontSize=12;fontColor=default;endArrow=none;endFill=0;startSize=8;endSize=8;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>

### 4.3 Action Arrow (blockThin direction)
Used in process layers for explicit step direction.

    <mxCell id="{{ID}}" value="" style="html=1;endArrow=blockThin;endFill=1;startArrow=none;rounded=0;startFill=0;fontSize=12;startSize=8;endSize=8;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>

### 4.4 Automated Action Variant (dashed)
Same as action arrow but dashed for automated/system flow.

    <mxCell id="{{ID}}" value="" style="html=1;startArrow=blockThin;startFill=1;endArrow=none;rounded=0;endFill=0;dashed=1;fontSize=12;startSize=8;endSize=8;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>

### 4.5 Plain Connector (no arrows)
Used between callout and actor/system without direction emphasis.

    <mxCell id="{{ID}}" value="" style="html=1;startArrow=none;startFill=0;endArrow=none;rounded=0;endFill=0;fontSize=12;startSize=8;endSize=8;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>

### 4.6 Orthogonal Connector with Waypoint
Used where curved links are less readable.

    <mxCell id="{{ID}}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;fontSize=12;startSize=8;endSize=8;" parent="1" source="{{SOURCE_ID}}" target="{{TARGET_ID}}" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="{{WAYPOINT_X}}" y="{{WAYPOINT_Y}}" />
        </Array>
      </mxGeometry>
    </mxCell>

## 5. Grouping

### 5.1 Logical Group Container
Use only for static move/select grouping where collapse/expand is not needed.

    <mxCell id="{{ID}}" connectable="0" parent="1" style="group" value="" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry" />
    </mxCell>

### 5.2 Expandable Group Container (default for element grouping)
Use as the default grouping block for Salesforce diagrams when elements are grouped by domain or layer.

    <mxCell id="{{ID}}" value="{{GROUP_TITLE}}" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#B3B3B3;arcSize=20;absoluteArcSize=1;collapsible=1;container=1;recursiveResize=1;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry">
        <mxRectangle x="{{X}}" y="{{Y}}" width="{{COLLAPSED_W}}" height="30" as="alternateBounds" />
      </mxGeometry>
    </mxCell>

### 5.3 Group Background Bar
Common with horizontal grouped strips (for example, inventory/products/orders/customers).

    <mxCell id="{{ID}}" parent="{{GROUP_ID}}" style="rounded=1;whiteSpace=wrap;html=1;fontSize=16;" value="" vertex="1">
      <mxGeometry width="{{W}}" height="{{H}}" as="geometry" />
    </mxCell>

### 5.4 Expandable/Resizable System Group
Large container used to hold nested panels and sections.

    <mxCell id="{{ID}}" value="{{GROUP_TITLE}}" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#B3B3B3;arcSize=20;absoluteArcSize=1;collapsible=1;container=1;recursiveResize=1;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry">
        <mxRectangle x="{{X}}" y="{{Y}}" width="{{COLLAPSED_W}}" height="30" as="alternateBounds" />
      </mxGeometry>
    </mxCell>

## 6. Other Reusable Blocks Found in Template

### 6.1 Process Callout Bubble
Used for event statements in Layer 3 and Layer 4.

    <mxCell id="{{ID}}" value="{{CALLOUT_TEXT}}" style="html=1;rounded=1;absoluteArcSize=1;arcSize=80;whiteSpace=wrap;fontSize=11;" parent="1" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="200" height="30" as="geometry" />
    </mxCell>

### 6.2 Legend Action Chip (tiny rounded label)
Used in Layer 4 legend for user action and automated chips.

    <mxCell id="{{ID}}" value="{{TEXT}}" style="html=1;rounded=1;absoluteArcSize=1;arcSize=80;whiteSpace=wrap;fontSize=11;" parent="{{HEADER_ID}}" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="74" height="14" as="geometry" />
    </mxCell>

### 6.3 Inner Neutral Panel
Subtle bordered block used inside larger process cards.

    <mxCell id="{{ID}}" value="" style="rounded=1;whiteSpace=wrap;html=1;fontSize=16;strokeColor=#E6E6E6;" parent="{{PARENT_ID}}" vertex="1">
      <mxGeometry x="{{X}}" y="{{Y}}" width="{{W}}" height="{{H}}" as="geometry" />
    </mxCell>

## 7. Style Notes (from template)

- Header backgrounds use `fillColor=#d9d9d9`.
- Channel/pill cards use `fillColor=#D9D9D9` and `strokeColor=none`.
- Main cards use rounded border style: `strokeColor=#B3B3B3;arcSize=20;absoluteArcSize=1`.
- Icon blocks usually include `aspect=fixed`, gray fill `#e5e5e5`, and a Salesforce `shape=mxgraph.salesforce.*2` icon.
- Text rows use `style="text;...;rounded=0"`.
- Integration mapping edges are usually `dashed=1`, while structural links are usually solid.
