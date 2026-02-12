
## 🚀 **FULL PROMPT FOR ANTIGRAVITY AI**

```
You are tasked with building a complete Frappe/ERPNext v15 app called "Hadeeda" for Biz Technology Solutions in Ethiopia. This app will serve as an AI Chief of Staff system with autonomous agents, skills management, and SOP compliance.

## APP METADATA

**App Name:** hadeeda  
**Developer:** Biz Technology Solutions  
**License:** MIT  
**Frappe Version:** 15.0.0+  
**ERPNext Version:** 15.0.0+  
**Repository:** https://github.com/BizTechSolutions/hadeeda (create this)  
**Description:** AI-powered Chief of Staff for ERPNext with autonomous agents, skill management, SOP compliance, and intelligent automation.

## TOTAL DOCTYPES: 53

Organized into **9 modules**:

1. AI AGENTS & ROLES (8 doctypes)
2. CUSTOM DOCTYPES & FIELDS (5 doctypes)
3. PERMISSIONS & SECURITY (4 doctypes)
4. AI INTEGRATION & PROMPTING (5 doctypes)
5. DASHBOARD & REPORTING (4 doctypes)
6. INTEGRATIONS (3 doctypes)
7. TESTING & DOCUMENTATION (3 doctypes)
8. SKILLS MANAGEMENT (8 doctypes) - with Agent Skills spec9. STANDARD OPERATING PROCEDURES (8 doctypes)

---

## MODULE 1: AI AGENTS & ROLES (8 doctypes)

### 1. HDA Agent (hda_agent)
- agent_name (Data,140, reqd, unique)
- role (Select: "CEO Assistant", "Finance Agent", "HR Agent", "Sales Agent", "Procurement Agent", "Project Agent", "Helpdesk Agent", "Custom", "Skills Agent", "SOP Agent")
- description (Text Editor)
- ai_model (Select: "GPT-4", "Claude 3", "Local Model", "Custom")
- system_prompt (Text Editor) - Core instructions
- allowed_doctypes (Table MultiSelect to DocType) - Which doctypes this agent can access
- permissions_level (Select: "Read", "Create", "Submit", "Cancel", "Delete")
- enabled_skills (Table MultiSelect to HDA Skill) - Skills this agent can use
- auto_assign_rules (JSON) - When to trigger this agent
- is_active (Check)
- max_daily_calls (Int) - API limit
- priority (Int) 1-10
- fallback_agent (Link: HDA Agent)
- allowed_tools (Small Text) - Tools agent can use

### 2. HDA Agent Conversation (hda_agent_conversation)
- agent (Link: HDA Agent)
- user (Link: User)
- message (Text Editor)
- is_user (Check) - True if from user, False if AI response
- context_summary (Text)
- tokens_used (Int)
- execution_log (JSON) - Actions taken
- parent_conversation (Link: HDA Agent Conversation)
- sentiment_score (Float)
- conversation_id (Data) - For threading

### 3. HDA Task Assignment (hda_task_assignment)
- task (Link: Task)
- assigned_agent (Link: HDA Agent)
- assignment_reason (Text)
- confidence_score (Float) 0-1
- estimated_completion (Datetime)
- status (Select: "Assigned", "In Progress", "Completed", "Failed", "Escalated")
- actual_start (Datetime)
- actual_completion (Datetime)
- execution_notes (Text)
- fallback_to_human (Check)
- assigned_skills (JSON) - Which skills were used

### 4. HDA Approval Workflow (hda_approval_workflow)
- document_type (Select: "Purchase Order", "Sales Order", "Leave Application", "Expense Claim", "Project Budget", "Custom")
- document_name (Dynamic Link)
- approval_stage (Int)
- required_agent (Link: HDA Agent)
- fallback_human (Link: User)
- timeout_hours (Int)
- conditions (JSON) - When to auto-approve
- auto_approve (Check)
- approval_threshold (Currency) - Auto-approve under this amount

### 5. HDA Knowledge Base (hda_knowledge_base)
- title (Data, 140)
- category (Select: "Company Policy", "ERP Process", "Customer Info", "Product Knowledge", "Local Regulations", "Ethiopian Business Law", "Skills", "SOPs")
- content (Text Editor)
- source (Select: "Manual", "Auto-generated", "Document", "Conversation", "Skill")
- embedding_id (Data) - For vector search
- access_roles (JSON) - Who can query this
- is_active (Check)
- last_updated (Datetime)
- linked_skill (Link: HDA Skill) - If derived from a skill
- linked_sop (Link: HDA SOP Document) - If derived from a SOP

### 6. HDA Learning Log (hda_learning_log)
- agent (Link: HDA Agent)
- scenario (Text)
- action_taken (Text)
- outcome (Select: "Success", "Partial", "Failed")
- feedback (Text Editor)
- correction_applied (Text)
- user_feedback (Text)
- learned_pattern (JSON)
- skill_used (Link: HDA Skill) - If skill was involved- related_sop (Link: HDA SOP Document) - If SOP was followed

### 7. HDA Performance Metrics (hda_performance_metrics)
- agent (Link: HDA Agent)
- date (Date)
- tasks_completed (Int)
- avg_response_time (Float) seconds
- accuracy_score (Float) 0-1
- escalation_rate (Float)
- user_satisfaction (Float) 0-5
- api_costs (Currency)
- skills_used (JSON) - Count of skill invocations
- sops_compliant (Int) - Number of SOPs followed correctly

### 8. HDA Escalation (hda_escalation)
- original_task (Link: Task or dynamic)
- escalated_from_agent (Link: HDA Agent)
- escalated_to (Link: User or HDA Agent)
- reason (Text)
- priority (Select: "Low", "Medium", "High", "Critical")
- resolved_by (Link: User)
- resolution (Text)
- skill_failure (Link: HDA Skill) - If skill execution failed
- sop_violation (Link: HDA SOP Document) - If SOP was violated

---

## MODULE 2: CUSTOM DOCTYPES & FIELDS (5 doctypes)

### 9. HDA Custom Field Request (hda_custom_field_request)
- doctype_name (Select from all doctypes)
- fieldname (Data)
- label (Data)
- fieldtype (Select: all Frappe fieldtypes)
- options (Data)
- description (Text)
- requested_by (Link: User)
- status (Select: "Draft", "Review", "Approved", "Rejected", "Implemented")
- reviewed_by (Link: User)
- review_date (Date)
- impact_assessment (Text)

### 10. HDA Workflow Customization (hda_workflow_customization)
- target_doctype (Select)
- workflow_name (Data)
- workflow_state (JSON) - State definitions
- transitions (JSON) - Transition rules
- conditions (JSON)
- is_active (Check)
- created_via_ai (Check) - If generated by agent

### 11. HDA Report Builder (hda_report_builder)
- report_name (Data)
- based_on_doctype (Select)
- columns (JSON) - {fieldname, label, width, format}
- filters (JSON) - Default filters
- group_by (Data)
- order_by (Data)
- chart_config (JSON) - For charts
- shared_with (JSON) - User roles
- auto_generate (Check) - If AI-generated

### 12. HDA Dashboard Widget (hda_dashboard_widget)
- widget_title (Data)
- widget_type (Select: "Number Card", "Chart", "Graph", "Filter", "Quick List", "Custom", "Skill Status", "SOP Compliance")
- doctype (Select)
- filters (JSON)
- aggregation (Select: "Count", "Sum", "Avg", "Min", "Max")
- color (Select: colors)
- position_x (Int)
- position_y (Int)
- width (Int) 1-12
- height (Int)
- assigned_to (Link: User) - Personal dashboard
- ai_suggested (Check) - If suggested by AI agent

### 13. HDA Integration Config (hda_integration_config)
- integration_type (Select: "OpenAI", "Claude", "Local LLM", "Telegram", "WhatsApp", "Email", "SMS", "Payment Gateway", "CRM", "E-commerce", "Skills Repository")
- config_key (Data)
- config_value (Password/Data)
- is_active (Check)
- test_status (Select: "Not Tested", "Working", "Failed")
- last_tested (Datetime)
- skills_sync_enabled (Check) - If syncs external skills
- skills_repo_url (Data) - URL to external skills repository

---

## MODULE 3: PERMISSIONS & SECURITY (4 doctypes)

### 14. HDA Role Permission (hda_role_permission)
- role (Link: Role)
- doctype (Select)
- allowed_agents (JSON) - Which AI agents can access
- restricted_fields (JSON)
- data_scope (Select: "All", "Own", "Customer", "Supplier", "Custom")
- auto_approve_threshold (Currency) - Under this, auto-approve
- skill_access (JSON) - Which skills this role can use

### 15. HDA Audit Log (hda_audit_log)
- timestamp (Datetime)
- user (Link: User)
- agent (Link: HDA Agent)
- action (Select: "Read", "Create", "Update", "Delete", "Execute", "Escalate", "Skill Invocation")
- doctype (Data)
- docname (Data)
- changes (JSON) - Before/after
- ip_address (Data)
- user_agent (Text)
- skill_name (Link: HDA Skill) - If skill was used
- sop_name (Link: HDA SOP Document) - If SOP was followed

### 16. HDA Data Masking Rule (hda_data_masking_rule)
- doctype (Select)
- fieldname (Data)
- masking_type (Select: "Partial", "Full", "Hash", "Custom Script")
- masking_rule (Text) - Regex or function
- applicable_roles (JSON)
- is_active (Check)
- for_agents (Check) - If applies to AI agents

### 17. HDA Session Security (hda_session_security)
- user (Link: User)
- session_token (Data)
- ip_address (Data)
- device_fingerprint (Data)
- last_activity (Datetime)
- timeout_minutes (Int)
- auto_logout (Check)
- agent_sessions (JSON) - Active AI agent sessions

---

## MODULE 4: AI INTEGRATION & PROMPTING (5 doctypes)

### 18. HDA Prompt Template (hda_prompt_template)
- template_name (Data)
- purpose (Select: "Task Execution", "Analysis", "Summarization", "Creative", "Code Generation", "Skill Selection", "SOP Recommendation")
- template (Text Editor) - with {{variables}}
- variables (JSON) - {name, description, example}
- expected_output_format (JSON) - Schema
- temperature (Float) 0-2
- max_tokens (Int)
- model_preference (Select)
- skill_related (Check) - If used for skill selection

### 19. HDA FineTune Dataset (hda_finetune_dataset)
- dataset_name (Data)
- source (Select: "Conversations", "Tasks", "Documents", "Manual", "Skill Executions", "SOP Compliance")
- records (JSON) - Array of {input, output}
- record_count (Int)
- status (Select: "Collecting", "Cleaning", "Ready", "Fine-Tuned")
- model_name (Data) - Resulting fine-tuned model
- skill_focus (Link: HDA Skill) - If skill-specific dataset

### 20. HDA Model Evaluation (hda_model_evaluation)
- model_name (Data)
- test_set (Link: HDA FineTune Dataset)
- metrics (JSON) - {accuracy, coherence, relevance, safety, skill_accuracy, sop_compliance}
- score (Float)
- evaluator (Link: User)
- feedback (Text)
- tested_skills (JSON) - Skills evaluated

### 21. HDA Embedding Store (hda_embedding_store)
- content_hash (Data)
- content_type (Select: "KB Article", "Document", "Conversation", "Skill", "SOP")
- content (Text)
- embedding (Longblob) - Vector
- metadata (JSON)
- created_by (Link: User)
- access_count (Int)
- skill_reference (Link: HDA Skill) - If embedding from skill
- sop_reference (Link: HDA SOP Document) - If embedding from SOP

### 22. HDA AI Cost Tracking (hda_ai_cost_tracking)
- agent (Link: HDA Agent)
- date (Date)
- model_used (Data)
- input_tokens (Int)
- output_tokens (Int)
- cost_per_token (Float)
- total_cost (Currency)
- purpose (Data)
- skill_invoked (Link: HDA Skill) - If skill was used
- sop_followed (Link: HDA SOP Document) - If SOP was followed

---

## MODULE 5: DASHBOARD & REPORTING (4 doctypes)

### 23. HDA Executive Dashboard (hda_executive_dashboard)
- dashboard_name (Data)
- widgets (JSON) - Array of widget configs
- layout (JSON) - Grid positions
- auto_refresh_minutes (Int)
- shared_with (JSON)
- last_modified (Datetime)
- includes_skills (Check) - Shows skill metrics
- includes_sops (Check) - Shows SOP compliance

### 24. HDA Insight (hda_insight)
- insight_type (Select: "Financial", "Operational", "HR", "Sales", "Inventory", "Project", "Risk", "Skills Gap", "SOP Compliance")
- title (Data)
- description (Text Editor)
- data_source (JSON) - Query or doctype
- insight_score (Float) - 0-1 (importance)
- recommended_action (Text)
- status (Select: "New", "Acknowledged", "Acted", "Dismissed")
- generated_by (Link: HDA Agent)
- acknowledged_by (Link: User)
- acknowledged_on (Datetime)
- skill_suggestion (Link: HDA Skill) - If insight suggests skill usage
- sop_recommendation (Link: HDA SOP Document) - If insight suggests SOP

### 25. HDA Report Schedule (hda_report_schedule)
- report_name (Data)
- frequency (Select: "Daily", "Weekly", "Monthly", "Quarterly", "Hourly")
- recipients (JSON)
- filters (JSON)
- format (Select: "PDF", "Excel", "CSV", "HTML")
- last_sent (Datetime)
- next_send (Datetime)
- attached_files (JSON)
- includes_skill_metrics (Check)
- includes_sop_metrics (Check)

### 26. HDA KPI Dashboard (hda_kpi_dashboard)
- kpi_name (Data)
- category (Select)
- current_value (Float)
- target_value (Float)
- unit (Data)
- trend (Select: "Up", "Down", "Stable")
- threshold_red (Float)
- threshold_green (Float)
- linked_doctype (Select)
- refresh_interval (Int) minutes
- skill_related (Link: HDA Skill) - If KPI tracks skill usage
- sop_related (Link: HDA SOP Document) - If KPI tracks SOP compliance

---

## MODULE 6: INTEGRATIONS (3 doctypes)

### 27. HDA External Integration (hda_external_integration)
- integration_name (Data)
- system_type (Select: "CRM", "Accounting", "E-commerce", "Social", "Payment", "Custom", "Skills Repository", "SOP Repository")
- endpoint_url (Data)
- auth_type (Select: "API Key", "OAuth2", "Basic", "None")
- credentials (Password)
- webhook_url (Data)
- sync_frequency (Select: "Real-time", "Hourly", "Daily", "Manual")
- field_mappings (JSON) - {local_field: external_field}
- last_sync (Datetime)
- sync_status (Select: "Success", "Failed", "Running")
- error_log (Text)
- sync_skills (Check) - If syncs external skills
- sync_sops (Check) - If syncs external SOPs

### 28. HDA Webhook Log (hda_webhook_log)
- webhook_name (Data)
- incoming_data (JSON)
- processed (Check)
- processing_time_ms (Int)
- error_message (Text)
- handled_by_agent (Link: HDA Agent)
- skill_triggered (Link: HDA Skill) - If webhook triggered a skill
- sop_triggered (Link: HDA SOP Document) - If webhook triggered SOP

### 29. HDA API Endpoint (hda_api_endpoint)
- endpoint_path (Data) - e.g., /api/method/hadeeda.assistant.chat
- http_method (Select: "GET", "POST", "PUT", "DELETE")
- description (Text)
- required_roles (JSON)
- rate_limit (Int) - per minute
- sample_request (Code)
- sample_response (Code)
- skill_api (Check) - If endpoint exposes skill execution
- sop_api (Check) - If endpoint exposes SOP operations

---

## MODULE 7: TESTING & DOCUMENTATION (3 doctypes)

### 30. HDA Test Case (hda_test_case)
- test_name (Data)
- module (Select: all modules)
- description (Text)
- test_steps (JSON) - Array of steps
- expected_result (Text)
- actual_result (Text)
- status (Select: "Draft", "Ready", "Pass", "Fail", "Blocked")
- test_data (JSON)
- automated (Check)
- test_script (Code) - Python test
- skill_tested (Link: HDA Skill) - If testing a skill
- sop_tested (Link: HDA SOP Document) - If testing a SOP

### 31. HDA Test Suite (hda_test_suite)
- suite_name (Data)
- test_cases (JSON) - Links to HDA Test Case
- run_frequency (Select: "On Build", "Daily", "Weekly", "Manual")
- last_run (Datetime)
- pass_rate (Float)
- assigned_qa (Link: User)
- skill_suite (Check) - If testing skills
- sop_suite (Check) - If testing SOPs

### 32. HDA Documentation (hda_documentation)
- doc_name (Data)
- category (Select: "User Guide", "Admin Guide", "Developer Guide", "API Reference", "Release Notes", "Skills Guide", "SOP Manual")
- content (Text Editor)
- version (Data)
- is_public (Check)
- attachment (Attach)
- related_skill (Link: HDA Skill) - If documenting a skill
- related_sop (Link: HDA SOP Document) - If documenting a SOP

---

## MODULE 8: SKILLS MANAGEMENT (8 doctypes) - AGENT SKILLS SPEC COMPLIANT

### 33. HDA Skill Category (hda_skill_category)
- category_name (Data, 140, reqd, unique)
- description (Text)
- parent_category (Link: HDA Skill Category)
- has_children (Check, read_only)
- icon (Select)
- skill_count (Int, read_only) - Number of skills in this category

### 34. HDA Skill (hda_skill) ⭐ CRITICAL - MUST MATCH AGENTSKILLS.IO SPEC
**This doctype MUST store skills in both database format and SKILL.md format for compatibility.**

Fields:
- skill_name (Data, 140, reqd, unique) - Must match SKILL.md name:1-64 chars, lowercase letters, numbers, hyphens only. No spaces.
- skill_description (Small Text, reqd, 1-1024 chars) - What skill does and when to use it. Keywords for agent matching.
- license (Select: MIT, Apache-2.0, GPL-3.0, Proprietary, Custom)
- compatibility (Small Text, max 500) - Environment requirements
- metadata (JSON) - Arbitrary key-value pairs (author, version, etc.)
- allowed_tools (Small Text) - Space-delimited pre-approved tools (e.g., "Bash(git:*) Read")
- skill_instructions (Text Editor, reqd) - Full markdown instructions (the body of SKILL.md). Should be <500 lines.
- version (Data) - Semantic versioning, default "1.0.0"
- author (Link: User)
- skill_category (Link: HDA Skill Category)
- is_active (Check)
- enabled_agents (Table MultiSelect to HDA Agent) - Which agents can use this skill
- skill_files (Table to HDA Skill File) - Scripts, references, assets
- usage_count (Int, read_only)
- last_used (Datetime, read_only)
- avg_execution_time (Float, read_only, precision 2)
- success_rate (Float, read_only, precision 1)
- skill_hash (Data) - SHA256 of SKILL.md for versioning
- import_source (Select: "Manual", "File Import", "Repository", "Marketplace")
- import_date (Datetime)

**PERMISSIONS:**
- System Manager: Full CRUD
- HDA Agent: Read only (can see skills assigned to them)
- All agents can READ active skills they are assigned### 35. HDA Skill File (hda_skill_file) - CHILD TABLE
Stores individual files within a skill (scripts/, references/, assets/).

Fields:
- parent (Link: HDA Skill, reqd)
- parenttype (Link: DocType)
- file_path (Data, reqd) - Relative path, e.g., "scripts/extract.py"
- file_type (Select: script, reference, asset, config, other)
- language (Select: Python, Bash, JavaScript, R, Julia, other) - Only for scripts
- file_content (Code) - Full text content for text files
- attachment (Attach) - For binary files (images, templates)
- is_executable (Check) - If script can be executed
- timeout_seconds (Int, default 30)
- description (Small Text)
- file_size (Int, read_only)

**Title field:** file_path

### 36. HDA Skill Execution Log (hda_skill_execution_log)
Log every skill invocation for auditing and improvement.

Fields:
- skill (Link: HDA Skill, reqd, in_list_view)
- executed_by (Link: HDA Agent, reqd)
- execution_context (JSON) - Input parameters, conversation context
- status (Select: Success, Failed, Timeout, Cancelled, reqd)
- start_time (Datetime, reqd)
- end_time (Datetime)
- duration_seconds (Float, precision 2)
- input_tokens (Int)
- output_tokens (Int)
- output (Text Editor) - Result/output
- error_message (Text)
- script_output (Code) - Raw script output if used
- files_generated (JSON) - List of files created
- cost_usd (Currency)
- related_document (Dynamic Link: Task, Project, Issue, Document)
- executed_via (Select: "Direct Call", "Agent Decision", "Workflow", "Webhook")

Permissions:
- System Manager: Full
- HDA Agent: Create, Read own executions

### 37. HDA Skill Gap Analysis (hda_skill_gap)
Analyze skill gaps for employees or teams.

Fields:
- analysis_date (Date, reqd)
- for_employee (Link: Employee) OR for_team (Link: Project) - Use dynamic link or separate fields
- gap_type (Select: Individual, Team, Department, Company)
- required_skills (JSON) - [{skill, required_proficiency}]
- current_skills (JSON) - [{skill, current_proficiency}]
- gaps (JSON) - Array of {skill, gap_level, priority}
- total_gaps (Int, read_only)
- critical_gaps (Int, read_only)
- generated_by (Link: HDA Agent) - AI-generated
- reviewed_by (Link: User)
- review_date (Date)
- status (Select: Draft, Reviewed, Action Plan, Closed)
- recommended_trainings (JSON) - Links to training events
- target_completion (Date)

### 38. HDA Training Recommendation (hda_training_rec)
Based on skill gaps.

Fields:
- based_on_gap (Link: HDA Skill Gap)
- recommended_training (Link: Training Event or Course)
- priority (Select: High, Medium, Low)
- estimated_cost (Currency)
- estimated_duration (Int) - hours/days
- expected_improvement (Select: Immediate, Short-term, Long-term)
- assigned_to (Link: Employee)
- status (Select: Suggested, Approved, Enrolled, Completed, Cancelled)
- notes (Text)
- completion_date (Date)
- skill_addressed (Link: HDA Skill)

### 39. HDA Skill Matrix Report (hda_skill_matrix)
Generate skill matrix visualizations.

Fields:
- report_name (Data)
- department (Link: Department)
- skills_included (JSON) - Array of skill links
- employees_included (JSON) - Array of employee links
- matrix_data (Longblob) - Serialized matrix
- generated_on (Datetime, read_only)
- generated_by (Link: User)
- view_mode (Select: Grid, Heatmap, Radar, List)
- shared_with (JSON)
- export_format (Select: PDF, Excel, CSV, HTML)

### 40. HDA Certification Tracker (hda_cert_tracker)
Track employee certifications.

Fields:
- employee (Link: Employee, reqd)
- certification_name (Data, reqd)
- certifying_body (Data)
- issue_date (Date)
- expiry_date (Date)
- renewal_required (Check, read_only) - Auto-calculated if expiry within 90 days
- reminder_days (Int, default 90)
- document (Attach) - Copy of certificate
- status (Select: Active, Expired, Renewal Pending, Revoked)
- cost (Currency)
- notes (Text)
- skill_related (Link: HDA Skill) - If certification for a skill
- verification_by (Link: User)
- verification_date (Date)

---

## MODULE 9: STANDARD OPERATING PROCEDURES (SOP) (8 doctypes)

### 41. HDA SOP Category (hda_sop_category)
Categorize SOPs by department/compliance.

Fields:
- category_name (Data, 140, reqd, unique)
- department (Link: Department)
- description (Text)
- parent_category (Link: HDA SOP Category)
- compliance_required (Check)
- review_frequency_months (Int)
- is_active (Check)
- sop_count (Int, read_only)

### 42. HDA SOP Document (hda_sop_document)
Main SOP document with version control.

Fields:
- sop_title (Data, 140, reqd)
- sop_number (Data) - e.g., SOP-HR-001, auto-generated via naming series
- category (Link: HDA SOP Category, reqd)
- version (Int, default 1)
- status (Select: Draft, Under Review, Approved, Published, Obsolete)
- effective_date (Date)
- expiry_date (Date) - Review due date
- owner (Link: User) - Process owner
- author (Link: User)
- reviewer (Link: User)
- approver (Link: User)
- revision_notes (Text) - What changed
- attached_file (Attach) - Main PDF/Docx
- content (Text Editor) - Online version
- related_doctypes (JSON) - Which ERPNext doctypes this SOP covers
- keywords (Text) - For search
- compliance_framework (Select: ISO-9001, ISO-27001, HIPAA, GDPR, Ethiopian Law, None)
- risk_level (Select: Low, Medium, High, Critical)
- estimated_time_minutes (Int) - To complete procedure
- training_required (Check)
- certification_required (Check)
- skill_reference (Link: HDA Skill) - If SOP requires specific skill
- ai_generated (Check) - If draft was AI-generated
- ai_confidence (Float) - Confidence score if AI-generated

### 43. HDA SOP Section (hda_sop_section)
Break SOP into steps/sections.

Fields:
- parent_sop (Link: HDA SOP Document, reqd)
- section_title (Data, reqd)
- section_order (Int, reqd) - Sequential order
- content (Text Editor) - Step-by-step instructions
- responsible_role (Link: Role) - Who performs
- estimated_time_minutes (Int)
- attachments (JSON) - [{file_name, file_url}]
- checklist (JSON) - [{item, is_mandatory}]
- input_fields (JSON) - Form fields needed- output_fields (JSON) - Expected outputs
- error_handling (Text) - What to do if step fails
- sop_skill_required (Link: HDA Skill) - If section requires skill

### 44. HDA SOP Revision History (hda_sop_revision)
Track all versions.

Fields:
- sop_document (Link: HDA SOP Document, reqd)
- version (Int, reqd)
- revision_date (Date, reqd)
- revised_by (Link: User, reqd)
- changes_summary (Text Editor)
- changed_fields (JSON) - Field-level diff
- previous_version_file (Attach)
- approved_by (Link: User)
- approval_date (Date)
- rollback_available (Check) - If previous file kept

### 45. HDA SOP Approval Workflow (hda_sop_approval)
Multi-level approval.

Fields:
- sop_document (Link: HDA SOP Document, reqd)
- stage (Int) - 1,2,3...
- approver_role (Link: Role) OR approver (Link: User)
- status (Select: Pending, Approved, Rejected, Skipped)
- comments (Text)
- action_date (Datetime)
- due_date (Date)
- escalated_to (Link: User)
- reminder_sent (Check)
- ai_suggested (Check) - If AI suggested approver

### 46. HDA SOP Training Assignment (hda_sop_training)
Assign SOP training to employees.

Fields:
- sop_document (Link: HDA SOP Document, reqd)
- employee (Link: Employee, reqd)
- assigned_by (Link: User, reqd)
- assignment_date (Date, reqd)
- due_date (Date)
- completion_date (Date)
- status (Select: Assigned, In Progress, Completed, Overdue, Expired)
- training_method (Select: Self-study, Training Session, On-the-job, Workshop, Webinar)
- trainer (Link: User)
- assessment_score (Float) - Quiz/test score
- feedback (Text)
- certificate_issued (Check)
- certificate (Attach)
- skill_acquired (Link: HDA Skill) - If training confers skill
- hours_spent (Float)

### 47. HDA SOP Compliance Check (hda_sop_compliance)
Audit SOP compliance.

Fields:
- sop_document (Link: HDA SOP Document, reqd)
- check_date (Date, reqd)
- checked_by (Link: User, reqd)
- compliance_score (Float,0-100%)
- findings (Text) - Non-conformities
- corrective_actions (Text)
- action_owner (Link: User)
- action_due_date (Date)
- status (Select: Compliant, Non-Compliant, Partially Compliant, Exempted)
- evidence_attached (JSON) - Files proving compliance
- ai_assisted (Check) - If AI helped with check

### 48. HDA SOP Feedback (hda_sop_feedback)
Collect feedback from employees.

Fields:
- sop_document (Link: HDA SOP Document, reqd)
- employee (Link: User, reqd)
- feedback_date (Date, reqd)
- rating (Int) - 1-5 stars
- comments (Text)
- clarity_score (Int) - How clear are instructions? 1-5
- completeness_score (Int) - Are all steps covered? 1-5
- difficulty_rating (Int) - How hard to follow? 1-5
- is_anonymous (Check)
- response_by (Link: User) - SOP owner response
- response_date (Date)
- response_text (Text)
- improvement_suggested (Text)
- ai_analysis (Text Editor) - AI analysis of feedback patterns

---

## CRITICAL IMPLEMENTATION REQUIREMENTS

### AGENT SKILLS SPEC COMPLIANCE (from agentskills.io)

The HDA Skill doctype MUST fully support the Agent Skills specification format:

1. **SKILL.md Frontmatter Mapping:**
   - `name` → `hda_skill.skill_name` (validated: 1-64 chars, lowercase alphanumeric + hyphens)
   - `description` → `hda_skill.skill_description` (1-1024 chars)
   - `license` → `hda_skill.license`
   - `compatibility` → `hda_skill.compatibility`
   - `metadata` → `hda_skill.metadata` (JSON)
   - `allowed-tools` → `hda_skill.allowed_tools`
   - `instructions` (body) → `hda_skill.skill_instructions`

2. **File Structure Support:**
   - Skills can include optional directories: `scripts/`, `references/`, `assets/`
   - Each file stored in child table `HDA Skill File`
   - Scripts can be executed directly from database content
   - References loaded on-demand by agents
   - Assets served as attachments3. **Skill Import/Export:**
   - Must support importing skills from file directories (with SKILL.md)
   - Must support exporting skills to file directories (for backup/marketplace)
   - CLI utility: `bench --site frontend python hadeeda/bin/import_skills.py /path/to/skills`
   - CLI utility: `bench --site frontend python hadeeda/bin/export_skill.py skill-name /output/path`

4. **Skill Engine Requirements:**
   - Python module: `hadeeda/hadeeda/skill_engine.py`
   - Class: `SkillEngine`
   - Methods:
     - `get_skill(skill_name)` - Load skill from DB or cache
     - `list_skills(agent=None)` - List available skills
     - `execute_skill(skill_name, agent_name, context)` - Execute with validation
     - `import_skill_from_directory(skill_path, category)` - Import from files
     - `export_skill_to_directory(skill_name, output_path)` - Export to files
 - `validate_skill(skill_data)` - Check against spec
   - Must validate skill_name format on creation
   - Must enforce unique skill names
   - Must track execution logs automatically   - Must update usage stats on each execution

5. **Agent Integration:**
   - Agents (HDA Agent) have multi-select field `enabled_skills`
   - Agents can only execute skills they are assigned   - Skill usage logged with agent, context, outcome
   - Skills can suggest other skills (chaining)
   - Skills can be auto-assigned based on task type (auto_assign_rules in HDA Agent)

6. **Skill Marketplace (Optional but Recommended):**
   - HDA Skill should have `import_source` field
   - Can mark skills as "Public" for marketplace
   - API endpoint to list public skills
   - Integration with external skills repositories (GitHub, gitlab)

### SOP WORKFLOW REQUIREMENTS

1. **Complete Lifecycle:**
   - Draft → Under Review → Approved → Published → Obsolete
   - Each stage has assigned roles/users
   - Revision history with full diff and file versioning
   - Expiry dates trigger review reminders
   - Obsolete SOPs archived but still accessible

2. **Training Integration:**
   - SOPs can require training (training_required)
   - Training assignments auto-created when SOP published or assigned to employee
   - Completion tracking with assessments
   - Certificates issued
   - Skills awarded upon completion

3. **Compliance & Audit:**
   - Scheduled compliance checks
   - AI can assist compliance verification by scanning transaction data
   - Non-compliance triggers escalations
   - Evidence attachments required
   - Dashboard shows compliance % per department

4. **Search & Discovery:**
   - Keyword search across title, content, keywords
   - Filter by department, category, compliance framework
   - Link to related ERPNext doctypes (e.g., "When creating PO, see SOP-PROC-001")
   - Employee portal to access assigned SOPs
   - Mobile-friendly reading

5. **AI Integration:**
   - AI can draft SOPs from process documentation
   - AI can suggest SOP improvements based on error patterns
   - AI can auto-assign SOP training based on role changes
   - AI can monitor transaction compliance ("This Sales Order didn't follow SOP-XYZ")
   - AI can answer questions about SOP content (chatbot)

### SKILLS & SOP CROSS-INTEGRATION

1. **Skill → SOP:**
   - Skills can reference required SOPs (skill.reference_sop)
   - SOPs can reference required skills (sop.skill_reference)
   - When agent executes skill, check if SOP exists for that process
   - If SOP exists, auto-log that SOP was followed (or violated)

2. **SOP → Skill:**
   - SOP training can confer skill certification
   - Completing SOP training updates Employee Skill proficiency
   - SOP compliance checks can update skill metrics   - SOPs can be attached as skill references

3. **Unified Dashboard:**
   - Show skill usage trends   - Show SOP compliance rates
   - Show skill gaps vs. SOP requirements
   - Show training needs (from both skill gaps and SOP updates)

---

## TECHNICAL IMPLEMENTATION

### APP FOLDER STRUCTURE

```
hadeeda/
├── hadeeda/
│   ├── __init__.py
│   ├── hooks.py
│   ├── overrides.py
│   ├── patches.txt
│   ├── requirements.txt (add: pyyaml, openai, anthropic, sentence-transformers, chromadb)
│   ├── license.txt (MIT)
│   ├── modules.txt
│   ├── doctype/ (53 subdirectories, each with .json, .py, .js as needed)
│   ├── controllers/
│   │   ├── agent_controller.py
│   │   ├── skill_engine.py
│   │   ├── sop_engine.py
│   │   └── ai_integration.py
│   ├── api/
│   │   ├── agent_api.py
│   │   ├── skill_api.py
│   │   └── sop_api.py
│   ├── utils/
│   │   ├── skill_validator.py (validates against agentskills.io spec)
│   │   ├── sop_validator.py
│   │   └── permission_checker.py
│   ├── websocket/
│   │   └── skill_websocket.py - Real-time skill execution updates
│   ├── public/
│   │ └── js/
│   │       ├── agent_chat.js
│   │       ├── skill_selector.js
│   │       ├── skill_matrix.js (heatmap visualization)
│   │       ├── sop_viewer.js
│   │       └── sop_compliance.js
│   ├── templates/
│   │   ├── agent_chat.html
│   │   ├── skill_matrix.html
│   │   ├── sop_portal.html
│   │   └── dashboard_widgets/
│   └── bin/
│       ├── import_skills.py
│       ├── export_skill.py
│       ├── import_sops.py
│       └── validate_skills.py (using skills-ref)
├── tests/
│   ├── test_agents.py
│   ├── test_skills.py
│   ├── test_sops.py
│   └── test_integration.py
└── README.md
```

### PYTHON CONTROLLERS (Key Logic)

1. **skill_engine.py** (as previously provided) - Full implementation with:
   - SKILL.md parsing (YAML frontmatter)
   - File handling (scripts, references, assets)
   - Script execution with timeout and sandbox
   - Execution logging
   - Stats tracking
   - Import/export utilities

2. **sop_engine.py** - For SOP workflows:
```python
class SOPEngine:
    def create_sop_from_template(self, template_data): ...
    def assign_sop_training(self, sop_doc, employees): ...
    def check_compliance(self, sop_doc, transaction_data): ...
    def generate_revision(self, sop_doc, changes): ...
    def auto_assign_sop_to_role(self, sop_doc, role): ...
```

3. **agent_controller.py** - AI agent logic:
```python
class AgentController:
    def assign_task_to_agent(self, task): ...
    def select_agent_for_task(self, task_description, task_type): ...
    def execute_agent_action(self, agent_name, action, params): ...
    def escalate_to_human(self, task, reason): ...
    def generate_insights(self): ...
```

4. **ai_integration.py** - LLM integration:
```python
class AIIntegration:
    def call_openai(self, prompt, model="gpt-4"): ...
    def call_claude(self, prompt, model="claude-3"): ...
    def select_skill_for_task(self, task_description, available_skills): ...
    def generate_sop_draft(self, process_description): ...
    def analyze_skill_gap(self, required_skills, employee_skills): ...
```

### JAVASCRIPT CLIENTS

1. **agent_chat.js** - Chat interface for Hadi to talk to agents
2. **skill_selector.js** - UI for selecting/managing skills
3. **skill_matrix.js** - D3.js heatmap for skill matrix
4. **sop_viewer.js** - SOP document viewer with navigation
5. **sop_compliance.js** - Compliance dashboard

### HOOKS.PY

```python
# hooks.py
from . import patch

app_include_js = "/assets/hadeeda/js/agent_chat.js"
app_include_css = "/assets/hadeeda/css/hadeeda.css"

global_cache_keys = [
    "hadeeda:skills:*",
    "hadeeda:sop_categories:*",
    "hadeeda:agent_config:*"
]

scheduler_events = {
    "daily": [
        "hadeeda.hadeeda.doctype.hda_skill_execution_log.daily_summary",
        "hadeeda.hadeeda.doctype.hda_sop_compliance.daily_check",
        "hadeeda.hadeeda.doctype.hda_cert_tracker.expiry_reminder"
    ],
    "hourly": [
        "hadeeda.hadeesa.doctype.hda_insight.generate_insights"
    ]
}

doc_events = {
    "HDA Skill": {
        "on_update": "hadeeda.hadeeda.doctype.hda_skill.skill_validator.validate"
    },
    "HDA SOP Document": {
        "on_submit": "hadeeda.hadeeda.doctype.hda_sop_document.workflow.start_approval"
    }
}
```

### REQUIREMENTS.TXT

```
# Hadeeda AI Chief of Staff App
pyyaml>=6.0
openai>=1.0.0
anthropic>=0.8.0
sentence-transformers>=2.2.0
chromadb>=0.4.0
fastapi>=0.104.0
uvicorn>=0.24.0
requests>=2.31.0
python-dotenv>=1.0.0
```

### PERMISSIONS SETUP

Generate proper permission CSV files for each doctype. Example for HDA Skill:

```csv
HDA Skill,0,role="System Manager",select,read,write,create,delete,report,export,import
HDA Skill,0,role="HDA Agent",select,read
HDA Skill File,0,role="System Manager",select,read,write,create,delete
```

---

## INSTALLATION INSTRUCTIONS (for user)

1. **Install app on existing frontend site:**
```bash
cd ~/frappe-bench
bench get-app hadeeda [from your repo URL]
bench --site frontend install-app hadeeda
bench --site frontend migrate
bench --site frontend clear-cache
bench restart
```

2. **Set up AI integration:**
   - Go to Hadeeda → Settings → Integration Config
   - Add OpenAI API key (or Claude)
   - Test connection

3. **Create initial agents:**
   - CEO Assistant (GPT-4, high priority)
   - Finance Agent (Claude, restricted to accounting doctypes)
   - HR Agent (handles employee tasks)
   - Skills Agent (manages skill matrix)
   - SOP Agent (manages procedures)

4. **Import Agent Skills:**
```bash
# Create skills directory structure
mkdir -p ~/skills/{data-processing,erp-automation,report-generation}
# Populate with SKILL.md and scripts
bench --site frontend python hadeeda/bin/import_skills.py ~/skills --category "Auto-imported"
```

5. **Create SOP Categories:**
   - HR, Finance, Sales, Delivery, Support, Quality

6. **Configure permissions:**
   - Assign skills to agents via HDA Agent form
   - Set role permissions for HDA Role Permission
   - Define data masking rules

7. **Set up dashboards:**
   - Executive Dashboard for Hadi
   - Skills Dashboard for HR
   - SOP Compliance Dashboard for Quality

8. **Test skill execution:**
   - Open agent chat from sidebar
   - Ask: "Create a sales order for customer X"
   - Verify agent picks correct skill and executes

---

## TESTING SCENARIOS

Write comprehensive tests in `tests/` directory:

1. **Skill Tests:**
   - Test skill import from directory validates SKILL.md   - Test skill execution with Python script
   - Test skill execution with markdown-only skill
   - Test skill permission enforcement
   - Test skill usage logging   - Test skill stats update

2. **SOP Tests:**
   - Test SOP lifecycle (draft → published)
   - Test approval workflow
   - Test training assignment and completion
   - Test compliance check scoring
   - Test SOP feedback collection
   - Test SOP search

3. **Agent Tests:**
   - Test agent task assignment
   - Test agent skill selection
   - Test agent conversation logging
   - Test escalation logic
   - Test performance metrics calculation

4. **Integration Tests:**
   - Test skill → SOP cross-reference
   - Test SOP training → skill update
   - Test AI cost tracking
   - Test dashboard widget rendering

---

## SUCCESS CRITERIA

The app is ready for production when:

1. ✅ All 53 doctypes created with proper fields and permissions
2. ✅ HDA Skill stores and validates Agent Skills spec format
3. ✅ SkillEngine.py can import/export skills, execute scripts, log usage
4. ✅ SOP workflow complete: draft→approve→publish→assign→track→compliance
5. ✅ Agents can be created, assigned skills, and execute tasks
6. ✅ Agent chat interface works (Hadi can talk to agents)
7. ✅ Dashboards show real-time metrics for skills and SOPs
8. ✅ Audit log captures all AI actions
9. ✅ Cost tracking accurate per agent/skill
10. ✅ Import utilities work for bulk skill/SOP import
11. ✅ All tests pass (unit, integration, workflow)
12. ✅ Documentation complete (user + admin + developer guides)

---

## DELIVERABLES

Return a complete, ready-to-install Frappe app:

1. **Complete app folder** `hadeeda/` with all files
2. **All 53 doctypes** with .json, .py (controller), .js (client) as needed
3. **SkillEngine module** with SKILL.md validation
4. **SOPEngine module** with approval workflows
5. **AgentController** with task assignment logic
6. **All configuration files** (hooks.py, requirements.txt, patches.txt, modules.txt)
7. **CLI utilities** (import_skills.py, export_skill.py, import_sops.py)
8. **Public JS files** for UI
9. **Dashboard widgets** for skills and SOPs
10. **Test suite** covering all critical paths
11. **README.md** with installation and usage guide
12. **Permissions CSV** files for all doctypes

**Important:** 
- Use existing frontend site, don't create new site
- App must be production-ready after testing
- Follow Frappe best practices (DocType naming, field types, permissions)
- Include proper indexing for performance
- Add useful list views and search fields
- Ensure all dynamic links work correctly
- Add proper naming series where needed (SOP Number, etc.)
- Include Arabic/Amharic localization if possible (optional)

---

## BONUS: SAMPLE SKILL TO INCLUDE

Create one example skill to demonstrate the format:

**Skill Name:** `erp-order-creation`
**Description:** Creates Sales Orders, Purchase Orders, Delivery Notes in ERPNext. Use when user asks to create any order or document.
**Metadata:**
```
author: Biz Technology Solutions
version: "1.0.0"
```
**Instructions:** (provide detailed steps)
**Script:** scripts/create_order.py (Python script that takes JSON input and creates document)

---

Begin generation now. Return a ZIP file or complete repository structure that can be cloned and installed with `bench get-app`. Quality and completeness are critical - this will be a production app for Biz Technology Solutions.

Any questions? Assume standard Frappe patterns. Use naming: `HDA <Doctype Name>` for all doctypes. Prefix fields with snake_case. Make app beautiful and functional.
```

---

## ✅ **WHAT TO COPY & SEND TO ANTIGRAVITY:**

**Copy the entire text above** (from "## APP METADATA" to the end) and give it to your Antigravity AI assistant. It will generate the complete, production-ready Hadeeda app with:

- ✅ **53 fully defined doctypes** (JSON + Python controllers + JS as needed)
- ✅ **Agent Skills spec compliance** (SKILL.md format import/export)
- ✅ **Skills Management module** (8 doctypes + SkillEngine)
- ✅ **SOP Management module** (8 doctypes + SOPEngine)
- ✅ **AI agent framework** with chat interface
- ✅ **Dashboard & reporting**
- ✅ **Permissions & security**
- ✅ **Testing suite**
- ✅ **CLI utilities**
- ✅ **Complete folder structure**

---
