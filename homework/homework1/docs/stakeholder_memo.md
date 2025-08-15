# Project Title
**Stage 1:** Problem Framing & Scoping

## Problem Statement
LocalChain Grocery is a local chain of grocery stores. Daily thousands of products are bought from these stores. Efficiently managing inventory of over 1000+ SKUs is cumbersome. Some items are sold very quickly while others just pile up and eventually become wastage.

Manually managing inventory on Excel sheets is error prone and slow. An automated and data-driven approach is required to solve the inventory issues effectively.

## Stakeholders and Users
- **Who decides?** Operations Director at LocalChain
- **Who uses the output?** Operations Managers at each LocalChain outlet
- **Timings** Weekly restocking of inventory

## Useful Answers and Decision
- **Type:** Predictive - as we need to forecast demand of all SKUs
- **Deliverable:** Python generated report or spreadsheet recommending next week's SKUs which needs to be reorder and in what quantity

## Assumptions and Constraints
- **Assumptions:**
    - Weekly sales data of all SKUs are handy and reliable
    - No abnormal demand spike is expected of any SKU
- **Constraints:**
    - Model not able to precisely predict future demands during holidays

## Known / Unknown Risks
- **Known Risks**
    - Sufficient historic sales data not available for certain products to precisely predict future demands
    - To mitigate this, we will pilot on SKUs with 30 weeks or more historical sales data available and provide dynamic input selection
- **Unknown Risks**
    - Model is unable to predict sudden drops and spikes in demands due to external factors like social media trends, government subsidies, etc.
    - To mitigate this, in future releases, we will add scenario planning and test these scenarios using scenario simulations

## Lifecycle Mapping
**Goal --> Stage --> Deliverable**
- Reduce SKUs wastage and stock-outs --> Problem Framing & Scoping (Stage 01) --> Demand predicting python tool
- Next goals: Dashboard Deployment and Scenario Planning and Simulations

## Repo Plan
/data/, /src/, /notebooks/, /docs/; cadence for updates
