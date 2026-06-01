# Salesforce Metadata API — Org Analysis Reference

## 1. Data Model

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Data Model | Defines custom and standard object configuration — labels, sharing model, deployment status. Standard objects appear here when customized | Custom Object | `objects` | `CustomObject` |
| Data Model | All fields on an object — type (Lookup, MasterDetail, Formula, Picklist, etc.), length, values, default values, formula definitions | Custom Field | `objects/<Object>/fields` | `CustomField` |
| Data Model | Object mapped to data stored in an external system via Salesforce Connect — identifiable by `__x` suffix. Stored as `CustomObject` | External Object | `objects` | `CustomObject` |

---

## 2. Role Hierarchy

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Role Hierarchy | Defines a position in the org hierarchy — contains `parentRole` reference (building the tree), object access levels for cases, contacts, opportunities, accounts | Role | `roles` | `Role` |
| Role Hierarchy | Root container for an Enterprise Territory Management v2 model — states: Planning, Active, Archived | Territory2 Model | `territory2Models` | `Territory2Model` |
| Role Hierarchy | Individual territory within a Territory2 Model — contains `parentTerritory2` reference for hierarchy traversal and territory type | Territory2 | `territory2Models/<Model>/territories` | `Territory2` |
| Role Hierarchy | Category/label applied to Territory2 nodes (e.g., "Named Account", "Geographic") | Territory2 Type | `territory2Types` | `Territory2Type` |
| Role Hierarchy | Org-level settings for Enterprise Territory Management — indicates whether ETM is enabled | Territory2 Settings | `settings` | `Territory2Settings` |
| Role Hierarchy | Legacy territory from original Territory Management v1 (deprecated — present only in older orgs) | Territory (Legacy) | `territories` | `Territory` |
| Role Hierarchy | Public groups used in sharing rules and manual sharing | Group | `groups` | `Group` |
| Role Hierarchy | Record queues for cases, leads, orders — queues own records and drive assignment routing | Queue | `queues` | `Queue` |
| Role Hierarchy | Groups allowing limited admin delegation to non-admin users | Delegate Group | `delegateGroups` | `DelegateGroup` |

---

## 3. Security Model

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Security Model | Primary user security template — object CRUD, field-level security (FLS), tab visibility, page layout assignments, app visibility, system permissions, login IP ranges, login hours | Profile | `profiles` | `Profile` |
| Security Model | Additive permissions granted on top of a profile — object permissions, FLS, system permissions, custom permission references | Permission Set | `permissionsets` | `PermissionSet` |
| Security Model | Bundle of multiple Permission Sets applied as a unit — simplifies job-function security management | Permission Set Group | `permissionsetgroups` | `PermissionSetGroup` |
| Security Model | Selectively removes permissions granted by other Permission Sets within a Permission Set Group | Muting Permission Set | `mutingpermissionsets` | `MutingPermissionSet` |
| Security Model | Named permissions checkable in Apex, Flows, and formulas — used to gate custom feature access per user | Custom Permission | `customPermissions` | `CustomPermission` |
| Security Model | **Primary org-wide defaults (OWD) file** — contains default access levels for Account, Case, Contact, Lead, Opportunity, Calendar, and other objects | Sharing Settings | `settings` | `SharingSettings` |
---

## 4. Business Logic

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Business Logic | Formula-based rules preventing record saves with invalid data — encodes business validation logic per object | Validation Rule | `objects/<Object>/validationRules` | `ValidationRule` |
| Business Logic | Rules for detecting and managing duplicate records — linked to Matching Rules | Duplicate Rule | `duplicateRules` | `DuplicateRule` |
| Business Logic | Field comparison criteria used by Duplicate Rules to identify duplicate records | Matching Rule | `matchingRules` | `MatchingRules` |
| Business Logic | Automatically assigns accounts to territories based on account field criteria (ETM v2) | Territory2 Rule | `territory2Models/<Model>/rules` | `Territory2Rule` |
| Business Logic | Container for all sharing rules on an object — one file per object (e.g., `Account.sharingRules-meta.xml`) | Sharing Rules | `sharingRules` | `SharingRules` |
| Business Logic | Shares records based on record ownership | Sharing Owner Rule | (child of SharingRules) | `SharingOwnerRule` |
| Business Logic | Shares records based on field values on the record | Sharing Criteria Rule | (child of SharingRules) | `SharingCriteriaRule` |
| Business Logic | Extends read-only record access to unauthenticated Experience Cloud guest users | Sharing Guest Rule | (child of SharingRules) | `SharingGuestRule` |
| Business Logic | Shares records based on territory membership | Sharing Territory Rule | (child of SharingRules) | `SharingTerritoryRule` |
| Business Logic | Restricts field access beyond standard FLS based on user criteria — introduced API v50.0 | Field Restriction Rule | `fieldRestrictionRules` | `FieldRestrictionRule` |
| Business Logic | Reduces record visibility for specific users based on filter criteria — scoped to specific profiles/permission sets | Restriction Rule | `restrictionRules` | `RestrictionRule` |
| Business Logic | Account relationship-based sharing rules — used in Financial Services Cloud and Health Cloud | Account Relationship Share Rule | `accountRelationshipShareRules` | `AccountRelationshipShareRule` |
| Business Logic | Server-side custom logic triggered on DML events (insert, update, delete, undelete) on sObjects | Apex Trigger | `triggers` | `ApexTrigger` |
| Business Logic | Custom server-side logic classes — includes REST services (`@RestResource`), batch jobs, schedulable jobs, queueable jobs | Apex Class | `classes` | `ApexClass` |
| Business Logic | Declarative automation — screen flows, record-triggered flows, scheduled flows, autolaunched flows, subflows. Includes HTTP Action callouts for integrations | Flow | `flows` | `Flow` |
| Business Logic | Flow category definitions — organizes flows into named categories | Flow Category | `flowCategories` | `FlowCategory` |
| Business Logic | Reusable UI components built on the Aura framework — used in Lightning App Builder, Experience Cloud, and utility bars | Aura Component Bundle | `aura` | `AuraDefinitionBundle` |
| Business Logic | Reusable UI components built on the LWC framework — the modern standard for custom Salesforce UI | Lightning Web Component | `lwc` | `LightningComponentBundle` |

---

## 5. Saleaforce Capabilities(or Products) Available on the Org

> **Detection strategy:** Use three complementary sources — (1) SOQL-queryable license sObjects, (2) standard Permission Sets auto-provisioned by Salesforce when a product is enabled, (3) product-specific Settings metadata types.

### 5a. License sObjects (SOQL — not Metadata API types, queried via REST/SOQL)

| Area | Description | Metadata Type | Source | API Name (sObject) |
|------|-------------|---------------|--------|-------------------|
| Products | Lists all user license types provisioned on the org with total and used counts (e.g., `Salesforce`, `Service Cloud`, `Data Cloud`) | User License | SOQL sObject | `UserLicense` |
| Products | Lists all add-on / feature permission set licenses with counts (e.g., `Data Cloud for Marketing`, `Field Service Lightning`, `CPQ`) — the most reliable product indicator | Permission Set License | SOQL sObject | `PermissionSetLicense` |

### 5b. Standard Permission Sets (Metadata API — auto-created by Salesforce when a product is provisioned)

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Products | Salesforce automatically creates system-managed Permission Sets when products are enabled (e.g., `ServiceCloudUser`, `SalesUser`, `FieldServiceStandardPermSet`). Their presence in the org confirms that the corresponding product license has been provisioned | Permission Set (standard/system) | `permissionsets` | `PermissionSet` |

### 5c. Org Settings (Metadata API — all in `settings` folder, file pattern: `<TypeName>.settings-meta.xml`)

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Products — Sales Cloud | Collaborative Forecasting enabled — primary Sales Cloud indicator | Forecasting Settings | `settings` | `ForecastingSettings` |
| Products — Sales Cloud | Opportunity teams, similar opportunities, Einstein Deal Insights | Opportunity Settings | `settings` | `OpportunitySettings` |
| Products — Sales Cloud | Salesforce Quotes enabled | Quote Settings | `settings` | `QuoteSettings` |
| Products — Sales Cloud | Agentforce for Sales feature flags | Sales Deal Agent Settings | `settings` | `SalesDealAgentSettings` |
| Products — Service Cloud | Email-to-Case, Web-to-Case, case assignment/auto-response, Omni-Channel for cases | Case Settings | `settings` | `CaseSettings` |
| Products — Service Cloud | Entitlements and Service Contracts enabled | Entitlement Settings | `settings` | `EntitlementSettings` |
| Products — Service Cloud | Salesforce Knowledge (KB) enabled | Knowledge Settings | `settings` | `KnowledgeSettings` |
| Products — Service Cloud | Classic Live Agent / Chat enabled | Live Agent Settings | `settings` | `LiveAgentSettings` |
| Products — Service Cloud / Omni-Channel | Omni-Channel intelligent routing enabled | Omni-Channel Settings | `settings` | `OmniChannelSettings` |
| Products — Service Cloud Voice | Native telephony integration (Amazon Connect) enabled | Service Cloud Voice Settings | `settings` | `ServiceCloudVoiceSettings` |
| Products — Field Service | Field Service Lightning provisioned and configured | Field Service Settings | `settings` | `FieldServiceSettings` |
| Products — Experience Cloud | Communities / Experience Cloud enabled in the org | Communities Settings | `settings` | `CommunitiesSettings` |
| Products — Experience Cloud / PRM | Partner Relationship Management (partner portals) enabled | PRM Core Settings | `settings` | `PrmCoreSettings` |
| Products — Industry Clouds | Financial Services Cloud, Health Cloud, Consumer Goods, Public Sector, Life Sciences feature flags | Industries Settings | `settings` | `IndustriesSettings` |
| Products — Automotive Cloud | Automotive Cloud feature flags | Industries Automotive Settings | `settings` | `IndustriesAutomotiveSettings` |
| Products — Loyalty Cloud | Loyalty Management enabled | Industries Loyalty Settings | `settings` | `IndustriesLoyaltySettings` |
| Products — Manufacturing Cloud | Manufacturing Cloud features enabled | Industries Manufacturing Settings | `settings` | `IndustriesManufacturingSettings` |
| Products — OmniStudio / Industry | OmniStudio (formerly Vlocity) components enabled — foundation of all native Industry Clouds | OmniStudio Settings | `settings` | `OmniStudioSettings` |
| Products — Marketing Cloud / MCAE | Marketing Cloud Account Engagement (Pardot) connected to org | Pardot Settings | `settings` | `PardotSettings` |
| Products — Order Management | B2B Commerce / Order Management Cloud enabled | Order Management Settings | `settings` | `OrderManagementSettings` |
| Products — Data Cloud | Data Cloud (CDP) org-level enablement toggle | Customer Data Platform Settings | `settings` | `CustomerDataPlatformSettings` |
| Products — Einstein / Agentforce | Einstein GPT, Copilot, and Agent feature flags | Einstein GPT Settings | `settings` | `EinsteinGptSettings` |
| Products — Workforce Engagement | Workforce Engagement Management (WEM/WFM) enabled | Workforce Engagement Settings | `settings` | `WorkforceEngagementSettings` |
| Products — General | Person Accounts enabled, and other org-wide flags not tied to a specific product | Org Settings | `settings` | `OrgSettings` |
| Products — Territory Mgmt | Enterprise Territory Management v2 enabled | Territory2 Settings | `settings` | `Territory2Settings` |

---

## 6. Integrations — Inbound (External Systems → Salesforce)

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Integration — Inbound | **Complete inbound integration registry.** Each Connected App represents an external system authorized to access Salesforce via OAuth 2.0, SAML, or OpenID Connect. Contains consumer key, OAuth scopes, callback URLs, IP restrictions. Reveals every application or system that has been granted API access to the org | Connected App | `connectedApps` | `ConnectedApp` |

---

## 7. Integrations — Outbound (Salesforce → External Systems)

| Area | Description | Metadata Type | Local Folder | API Name |
|------|-------------|---------------|--------------|----------|
| Integration — Outbound | Stores authenticated endpoint URLs for outbound callouts. The definitive registry of every external API endpoint that Salesforce calls — used from Apex, Flows, and External Services | Named Credential | `namedCredentials` | `NamedCredential` |
| Integration — Outbound | Separates authentication protocol (OAuth 2.0, JWT, Named Principal, Per-User) from the endpoint URL — paired with Named Credentials. Reveals the auth mechanisms used for each outbound integration | External Credential | `externalCredentials` | `ExternalCredential` |
| Integration — Outbound | **Complete allowlist of all permitted outbound HTTP targets.** Every external URL callable from Apex or Flows must be registered here — covers all external systems regardless of whether a Named Credential exists | Remote Site Setting | `remoteSiteSettings` | `RemoteSiteSetting` |
