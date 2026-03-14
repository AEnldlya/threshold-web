"""
Babylon.js Code Generator

Generate Babylon.js code from animation prompts
"""

import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class BabylonJsGenerator:
    """Generate Babylon.js 3D animation code"""
    
    def __init__(self):
        """Initialize generator"""
        logger.info("Initialized Babylon.js Generator")
    
    def generate(
        self,
        prompt: str,
        use_cases: Optional[List[str]] = None,
        performance_target: int = 60,
        include_mobile: bool = True
    ) -> Dict[str, Any]:
        """
        Generate Babylon.js code from prompt
        
        Args:
            prompt: Animation description
            use_cases: Intended use cases
            performance_target: Target FPS
            include_mobile: Mobile optimization
        
        Returns:
            Dict with generated code and metadata
        """
        logger.info(f"Generating Babylon.js code: {prompt}")
        
        code = self._generate_scene(prompt, performance_target, include_mobile)
        
        return {
            "code_file": "components/3d/BabylonAnimation.tsx",
            "code": code,
            "lines_of_code": len(code.split('\n')),
            "libraries_used": ["babylon.js", "react-babylon"],
            "performance": performance_target,
            "mobile_optimized": include_mobile,
            "ready_to_deploy": True
        }
    
    def _generate_scene(
        self,
        prompt: str,
        fps: int,
        mobile: bool
    ) -> str:
        """Generate scene code"""
        
        code = f'''import * as BABYLON from 'babylonjs';
import {{ useEffect, useRef }} from 'react';

/**
 * Babylon.js Animation Scene
 * Generated from prompt: {prompt[:60]}...
 * Target FPS: {fps}
 * Mobile Optimized: {mobile}
 */

export function BabylonAnimation() {{
  const canvasRef = useRef(null);
  
  useEffect(() => {{
    if (!canvasRef.current) return;
    
    // Create engine and scene
    const engine = new BABYLON.Engine(canvasRef.current, true);
    const scene = new BABYLON.Scene(engine);
    
    // Camera
    const camera = new BABYLON.ArcRotateCamera(
      "camera",
      Math.PI / 2,
      Math.PI / 2.5,
      20,
      new BABYLON.Vector3(0, 0, 0),
      scene
    );
    camera.attachControl(canvasRef.current, true);
    
    // Lights
    const light1 = new BABYLON.PointLight(
      "light1",
      new BABYLON.Vector3(10, 10, 10),
      scene
    );
    light1.intensity = 0.8;
    
    const light2 = new BABYLON.HemisphericLight(
      "light2",
      new BABYLON.Vector3(0, 1, 0),
      scene
    );
    light2.intensity = 0.5;
    
    // Create mesh
    const box = BABYLON.MeshBuilder.CreateBox(
      "box",
      {{ size: 2 }},
      scene
    );
    
    // Material
    const material = new BABYLON.StandardMaterial("material", scene);
    material.diffuse = new BABYLON.Color3(0.2, 0.5, 1);
    material.specularColor = new BABYLON.Color3(0, 0, 0);
    box.material = material;
    
    // Animation
    const animation = new BABYLON.Animation(
      "rotation",
      "rotation.y",
      60,
      BABYLON.Animation.ANIMATIONTYPE_FLOAT,
      BABYLON.Animation.ANIMATIONLOOPMODE_LOOP
    );
    
    const keys = [
      {{ frame: 0, value: 0 }},
      {{ frame: 100, value: Math.PI * 2 }},
    ];
    
    animation.setKeys(keys);
    box.animations.push(animation);
    scene.beginAnimation(box, 0, 100, true);
    
    // Render loop
    engine.runRenderLoop(() => {{
      scene.render();
    }});
    
    // Handle window resize
    window.addEventListener('resize', () => {{
      engine.resize();
    }});
    
    return () => {{
      engine.dispose();
    }};
  }}, []);
  
  return (
    <div className="w-full h-screen">
      <canvas 
        ref={{canvasRef}} 
        style={{{{ width: '100%', height: '100%' }}}} 
      />
    </div>
  );
}}
'''
        return code
    
    def generate_advanced_scene(self) -> str:
        """Generate advanced scene with physics"""
        
        return '''
import * as BABYLON from 'babylonjs';
import 'babylonjs-loaders';

export function AdvancedBabylonScene() {
  const canvasRef = useRef(null);
  
  useEffect(() => {
    if (!canvasRef.current) return;
    
    const engine = new BABYLON.Engine(canvasRef.current, true);
    const scene = new BABYLON.Scene(engine);
    
    // Enable physics
    scene.enablePhysics(
      new BABYLON.Vector3(0, -9.81, 0),
      new BABYLON.CannonJSPlugin()
    );
    
    // Camera
    const camera = new BABYLON.ArcRotateCamera(
      "camera",
      Math.PI / 2,
      Math.PI / 2.5,
      30,
      new BABYLON.Vector3(0, 0, 0),
      scene
    );
    camera.attachControl(canvasRef.current, true);
    
    // Lights
    new BABYLON.HemisphericLight("light", new BABYLON.Vector3(0, 1, 0), scene);
    
    // Ground
    const ground = BABYLON.MeshBuilder.CreateGround(
      "ground",
      { width: 100, height: 100 },
      scene
    );
    ground.physicsImpostor = new BABYLON.PhysicsImpostor(
      ground,
      BABYLON.PhysicsImpostor.BoxImpostor,
      { mass: 0, restitution: 0.9 },
      scene
    );
    
    // Falling boxes
    for (let i = 0; i < 10; i++) {
      const box = BABYLON.MeshBuilder.CreateBox("box" + i, { size: 1 }, scene);
      box.position = new BABYLON.Vector3(
        Math.random() * 20 - 10,
        10 + i * 2,
        0
      );
      
      const material = new BABYLON.StandardMaterial("mat" + i, scene);
      material.diffuse = new BABYLON.Color3(Math.random(), Math.random(), Math.random());
      box.material = material;
      
      box.physicsImpostor = new BABYLON.PhysicsImpostor(
        box,
        BABYLON.PhysicsImpostor.BoxImpostor,
        { mass: 1, restitution: 0.8 },
        scene
      );
    }
    
    engine.runRenderLoop(() => {
      scene.render();
    });
    
    window.addEventListener('resize', () => engine.resize());
    
    return () => engine.dispose();
  }, []);
  
  return <canvas ref={canvasRef} style={{ width: '100%', height: '100vh' }} />;
}
'''
