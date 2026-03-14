"""State manager - Track deployment state and enable resumable flows."""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class StateManager:
    """Manages deployment state across steps."""
    
    def __init__(self, workflow_id: str, state_dir: str = ".deployment_state"):
        """Initialize state manager.
        
        Args:
            workflow_id: Unique identifier for this deployment workflow
            state_dir: Directory to store state files
        """
        self.workflow_id = workflow_id
        self.state_dir = Path(state_dir)
        self.state_dir.mkdir(exist_ok=True)
        self.state_file = self.state_dir / f"{workflow_id}.json"
        self._ensure_state_exists()
    
    def _ensure_state_exists(self):
        """Ensure state file exists."""
        if not self.state_file.exists():
            initial_state = {
                "workflow_id": self.workflow_id,
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "steps": {},
                "status": "pending",
                "metadata": {}
            }
            self.state_file.write_text(json.dumps(initial_state, indent=2))
    
    def save_step(self, step_name: str, data: Dict[str, Any]):
        """Save data for a step.
        
        Args:
            step_name: Name of the step
            data: Step data to save
        """
        state = self._read_state()
        state["steps"][step_name] = {
            "data": data,
            "timestamp": datetime.now().isoformat()
        }
        state["updated_at"] = datetime.now().isoformat()
        self._write_state(state)
        logger.info(f"Saved step: {step_name}")
    
    def get_step(self, step_name: str) -> Optional[Dict[str, Any]]:
        """Get data for a step.
        
        Args:
            step_name: Name of the step
        
        Returns:
            Step data or None
        """
        state = self._read_state()
        if step_name in state["steps"]:
            return state["steps"][step_name].get("data")
        return None
    
    def has_step(self, step_name: str) -> bool:
        """Check if a step has been completed.
        
        Args:
            step_name: Name of the step
        
        Returns:
            True if step exists
        """
        state = self._read_state()
        return step_name in state["steps"]
    
    def set_status(self, status: str):
        """Set overall workflow status.
        
        Args:
            status: Status value (pending, in_progress, completed, failed, cancelled)
        """
        state = self._read_state()
        state["status"] = status
        state["updated_at"] = datetime.now().isoformat()
        self._write_state(state)
        logger.info(f"Status: {status}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get workflow status.
        
        Returns:
            Current status
        """
        state = self._read_state()
        return {
            "workflow_id": state["workflow_id"],
            "status": state["status"],
            "created_at": state["created_at"],
            "updated_at": state["updated_at"],
            "completed_steps": list(state["steps"].keys()),
            "step_count": len(state["steps"])
        }
    
    def get_all_steps(self) -> Dict[str, Any]:
        """Get all steps data.
        
        Returns:
            Dictionary of all steps
        """
        state = self._read_state()
        result = {}
        for step_name, step_data in state["steps"].items():
            result[step_name] = step_data["data"]
        return result
    
    def can_resume_from(self, step_name: str) -> bool:
        """Check if workflow can resume from a specific step.
        
        Args:
            step_name: Step name to resume from
        
        Returns:
            True if resumable
        """
        # Check if we have state from before this step
        steps = self.get_all_steps()
        
        resumable_steps = [
            "deployed",
            "domains_searched",
            "domain_purchased"
        ]
        
        return any(s in steps for s in resumable_steps if s <= step_name)
    
    def get_cost_summary(self) -> Dict[str, float]:
        """Get cost summary from saved steps.
        
        Returns:
            Cost breakdown
        """
        steps = self.get_all_steps()
        costs = {
            "domain": 0.0,
            "deployment": 0.0,
            "total": 0.0
        }
        
        # Extract costs from steps
        if "domain_purchased" in steps:
            domain_data = steps["domain_purchased"]
            costs["domain"] = float(domain_data.get("cost", 0))
        
        costs["total"] = costs["domain"]
        
        return costs
    
    def get_timeline(self) -> list:
        """Get timeline of events.
        
        Returns:
            List of events with timestamps
        """
        state = self._read_state()
        timeline = []
        
        for step_name, step_data in state["steps"].items():
            timeline.append({
                "step": step_name,
                "timestamp": step_data["timestamp"]
            })
        
        # Sort by timestamp
        timeline.sort(key=lambda x: x["timestamp"])
        
        return timeline
    
    def _read_state(self) -> Dict[str, Any]:
        """Read state from file.
        
        Returns:
            State dictionary
        """
        try:
            content = self.state_file.read_text()
            return json.loads(content)
        except Exception as e:
            logger.error(f"Error reading state: {e}")
            return self._default_state()
    
    def _write_state(self, state: Dict[str, Any]):
        """Write state to file.
        
        Args:
            state: State dictionary
        """
        try:
            self.state_file.write_text(json.dumps(state, indent=2))
        except Exception as e:
            logger.error(f"Error writing state: {e}")
    
    def _default_state(self) -> Dict[str, Any]:
        """Get default state structure.
        
        Returns:
            Default state
        """
        return {
            "workflow_id": self.workflow_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "steps": {},
            "status": "pending",
            "metadata": {}
        }
    
    def rollback_to_step(self, step_name: str):
        """Rollback to a specific step, removing later steps.
        
        Args:
            step_name: Step to rollback to
        """
        state = self._read_state()
        
        # Keep only steps up to and including step_name
        new_steps = {}
        for name, data in state["steps"].items():
            new_steps[name] = data
            if name == step_name:
                break
        
        state["steps"] = new_steps
        state["updated_at"] = datetime.now().isoformat()
        self._write_state(state)
        logger.info(f"Rolled back to step: {step_name}")
    
    def clear(self):
        """Clear all state for this workflow."""
        if self.state_file.exists():
            self.state_file.unlink()
        self._ensure_state_exists()
        logger.info(f"Cleared state for workflow: {self.workflow_id}")
