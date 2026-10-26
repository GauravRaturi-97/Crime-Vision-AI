/**
 * CrimeVision AI - Interactive Three.js 3D Crime Scene Reconstruction
 * Lead Architect: Gaurav Raturi | SmartBridge EL Capstone Project
 */

class CrimeScene3D {
    constructor(canvasContainerId) {
        this.container = document.getElementById(canvasContainerId);
        if (!this.container) {
            console.error("3D Container element not found:", canvasContainerId);
            return;
        }

        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.controls = null;
        this.markers = [];
        this.raycaster = new THREE.Raycaster();
        this.mouse = new THREE.Vector2();
        this.trajectoryLine = null;
        this.pulseSphere = null;
        this.pathCurve = null;
        this.pulseProgress = 0;

        this.init();
        this.buildEnvironment();
        this.setupEventListeners();
        this.animate();
    }

    init() {
        // Scene setup
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x070b14);
        this.scene.fog = new THREE.FogExp2(0x070b14, 0.025);

        // Camera setup
        const aspect = this.container.clientWidth / this.container.clientHeight;
        this.camera = new THREE.PerspectiveCamera(45, aspect, 0.1, 1000);
        this.camera.position.set(16, 14, 18);

        // Renderer setup
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        this.container.appendChild(this.renderer.domElement);

        // OrbitControls
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.05;
        this.controls.maxPolarAngle = Math.PI / 2.05; // Prevent camera under floor
        this.controls.minDistance = 5;
        this.controls.maxDistance = 60;
        this.controls.target.set(0, 0, 0);

        // Lighting
        const ambientLight = new THREE.AmbientLight(0x38bdf8, 0.35);
        this.scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xffffff, 0.85);
        dirLight.position.set(20, 30, 15);
        dirLight.castShadow = true;
        dirLight.shadow.mapSize.width = 2048;
        dirLight.shadow.mapSize.height = 2048;
        this.scene.add(dirLight);

        // Grid Floor
        const grid = new THREE.GridHelper(32, 32, 0x38bdf8, 0x1e293b);
        grid.position.y = 0;
        this.scene.add(grid);

        // Subsurface Floor
        const floorGeo = new THREE.PlaneGeometry(36, 36);
        const floorMat = new THREE.MeshStandardMaterial({
            color: 0x090d16,
            roughness: 0.85,
            metalness: 0.1
        });
        const floor = new THREE.Mesh(floorGeo, floorMat);
        floor.rotation.x = -Math.PI / 2;
        floor.position.y = -0.05;
        floor.receiveShadow = true;
        this.scene.add(floor);
    }

    buildEnvironment() {
        // Architectural Volumes: Transit Terminal Main Building
        const terminalGeo = new THREE.BoxGeometry(10, 4.5, 6);
        const terminalMat = new THREE.MeshStandardMaterial({
            color: 0x1e293b,
            roughness: 0.7,
            metalness: 0.2
        });
        const terminal = new THREE.Mesh(terminalGeo, terminalMat);
        terminal.position.set(-6, 2.25, 0);
        terminal.castShadow = true;
        terminal.receiveShadow = true;
        this.scene.add(terminal);

        // Terminal Roof Lighting Band
        const bandGeo = new THREE.BoxGeometry(10.2, 0.3, 6.2);
        const bandMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
        const band = new THREE.Mesh(bandGeo, bandMat);
        band.position.set(-6, 4.5, 0);
        this.scene.add(band);

        // North Stairwell Structure
        const stairGeo = new THREE.BoxGeometry(3, 3.5, 3);
        const stairMat = new THREE.MeshStandardMaterial({ color: 0x334155 });
        const stair = new THREE.Mesh(stairGeo, stairMat);
        stair.position.set(-6, 1.75, 4);
        stair.castShadow = true;
        this.scene.add(stair);

        // Loading Dock / Vehicle Staging Bay
        const dockGeo = new THREE.BoxGeometry(8, 0.6, 6);
        const dockMat = new THREE.MeshStandardMaterial({ color: 0x172554 });
        const dock = new THREE.Mesh(dockGeo, dockMat);
        dock.position.set(7, 0.3, -3);
        dock.receiveShadow = true;
        this.scene.add(dock);

        // Parked Getaway Vehicle Representation
        const carBodyGeo = new THREE.BoxGeometry(3.6, 1.2, 1.8);
        const carMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.3, metalness: 0.8 });
        const car = new THREE.Mesh(carBodyGeo, carMat);
        car.position.set(7, 0.9, -3);
        car.castShadow = true;
        this.scene.add(car);

        // Headlights
        const lightGeo = new THREE.SphereGeometry(0.12, 16, 16);
        const lightMat = new THREE.MeshBasicMaterial({ color: 0xfef08a });
        const hl1 = new THREE.Mesh(lightGeo, lightMat);
        hl1.position.set(8.8, 0.9, -2.4);
        const hl2 = new THREE.Mesh(lightGeo, lightMat);
        hl2.position.set(8.8, 0.9, -3.6);
        this.scene.add(hl1);
        this.scene.add(hl2);

        // Default Suspect Trajectory
        this.buildTrajectory([
            [-6.0, 0.2, 4.0],
            [-3.5, 0.2, 3.0],
            [0.0, 0.2, 1.2],
            [3.5, 0.2, -0.8],
            [7.0, 0.2, -3.0],
            [12.0, 0.2, -5.5]
        ]);

        // Default Forensic Markers
        this.addEvidenceMarker("EV-01", "North Stairwell Egress", [-6.0, 0.5, 4.0], 0x38bdf8, "Point where subject exited holding metallic briefcase at 21:40 UTC.");
        this.addEvidenceMarker("EV-02", "Acoustic Transient Origin", [-1.5, 0.5, 1.0], 0xef4444, "Whisper & acoustic peak origin consistent with transient discharge.");
        this.addEvidenceMarker("EV-03", "Vehicle Staging / Getaway Vector", [7.0, 0.5, -3.0], 0xf59e0b, "Dark sedan staging location and flight vector eastbound onto State Ave.");
    }

    addEvidenceMarker(id, title, pos, hexColor, description) {
        const group = new THREE.Group();
        group.position.set(pos[0], pos[1], pos[2]);

        // Pin Pole
        const poleGeo = new THREE.CylinderGeometry(0.06, 0.06, 1.4, 16);
        const poleMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.8 });
        const pole = new THREE.Mesh(poleGeo, poleMat);
        pole.position.y = 0.7;
        pole.castShadow = true;
        group.add(pole);

        // Marker Head (Glowing Sphere)
        const headGeo = new THREE.SphereGeometry(0.35, 24, 24);
        const headMat = new THREE.MeshStandardMaterial({
            color: hexColor,
            emissive: hexColor,
            emissiveIntensity: 0.6,
            roughness: 0.2
        });
        const head = new THREE.Mesh(headGeo, headMat);
        head.position.y = 1.4;
        head.castShadow = true;
        group.add(head);

        // Marker Pulse Ring
        const ringGeo = new THREE.RingGeometry(0.3, 0.7, 32);
        const ringMat = new THREE.MeshBasicMaterial({
            color: hexColor,
            side: THREE.DoubleSide,
            transparent: true,
            opacity: 0.5
        });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.rotation.x = -Math.PI / 2;
        ring.position.y = 0.02;
        group.add(ring);

        // Metadata storage
        group.userData = {
            id: id,
            title: title,
            description: description,
            initialY: pos[1],
            headMesh: head
        };

        this.scene.add(group);
        this.markers.push(group);
    }

    buildTrajectory(pointsArray) {
        if (this.trajectoryLine) {
            this.scene.remove(this.trajectoryLine);
        }
        if (this.pulseSphere) {
            this.scene.remove(this.pulseSphere);
        }

        const vectors = pointsArray.map(p => new THREE.Vector3(p[0], p[1] + 0.1, p[2]));
        this.pathCurve = new THREE.CatmullRomCurve3(vectors);

        // Tube Geometry along path
        const tubeGeo = new THREE.TubeGeometry(this.pathCurve, 64, 0.08, 8, false);
        const tubeMat = new THREE.MeshBasicMaterial({
            color: 0xf59e0b,
            wireframe: false,
            transparent: true,
            opacity: 0.75
        });
        this.trajectoryLine = new THREE.Mesh(tubeGeo, tubeMat);
        this.scene.add(this.trajectoryLine);

        // Traveling Pulse Indicator
        const pulseGeo = new THREE.SphereGeometry(0.25, 16, 16);
        const pulseMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        this.pulseSphere = new THREE.Mesh(pulseGeo, pulseMat);
        this.scene.add(this.pulseSphere);
    }

    updateFromBackend(sceneData) {
        if (!sceneData) return;

        // Clear existing markers
        this.markers.forEach(m => this.scene.remove(m));
        this.markers = [];

        // Add markers from backend
        if (sceneData.evidence_markers) {
            sceneData.evidence_markers.forEach(em => {
                const hex = parseInt(em.color.replace("#", "0x"), 16);
                this.addEvidenceMarker(em.id, em.title, em.position, hex, em.description);
            });
        }

        // Add suspect trajectory path
        if (sceneData.suspect_path) {
            this.buildTrajectory(sceneData.suspect_path);
        }
    }

    setupEventListeners() {
        window.addEventListener("resize", () => {
            if (!this.container) return;
            const width = this.container.clientWidth;
            const height = this.container.clientHeight;
            this.camera.aspect = width / height;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(width, height);
        });

        this.container.addEventListener("click", (event) => {
            const rect = this.container.getBoundingClientRect();
            this.mouse.x = ((event.clientX - rect.left) / this.container.clientWidth) * 2 - 1;
            this.mouse.y = -((event.clientY - rect.top) / this.container.clientHeight) * 2 + 1;

            this.raycaster.setFromCamera(this.mouse, this.camera);
            const intersects = this.raycaster.intersectObjects(this.markers, true);

            if (intersects.length > 0) {
                // Find parent marker group
                let obj = intersects[0].object;
                while (obj.parent && !obj.userData.id) {
                    obj = obj.parent;
                }
                if (obj.userData.id) {
                    this.onMarkerSelected(obj.userData);
                }
            }
        });
    }

    onMarkerSelected(meta) {
        const infoBox = document.getElementById("selected-marker-info");
        if (infoBox) {
            infoBox.innerHTML = `
                <div style="border-left: 3px solid #38bdf8; padding-left: 10px;">
                    <div style="font-weight: 800; color: #38bdf8; font-size: 0.95rem;">[${meta.id}] ${meta.title}</div>
                    <div style="font-size: 0.82rem; color: #e2e8f0; margin-top: 4px;">${meta.description}</div>
                </div>
            `;
        }
    }

    setPresetCamera(view) {
        if (view === "overview") {
            this.camera.position.set(16, 14, 18);
            this.controls.target.set(0, 0, 0);
        } else if (view === "top") {
            this.camera.position.set(0, 26, 0.1);
            this.controls.target.set(0, 0, 0);
        } else if (view === "egress") {
            this.camera.position.set(-6, 4, 8);
            this.controls.target.set(-6, 1, 4);
        } else if (view === "vehicle") {
            this.camera.position.set(7, 4, 2);
            this.controls.target.set(7, 1, -3);
        }
    }

    animate() {
        requestAnimationFrame(() => this.animate());

        // Marker gentle bobbing animation
        const time = performance.now() * 0.003;
        this.markers.forEach((m, idx) => {
            if (m.userData.headMesh) {
                m.userData.headMesh.position.y = 1.4 + Math.sin(time + idx) * 0.08;
            }
        });

        // Trajectory Pulse Particle
        if (this.pathCurve && this.pulseSphere) {
            this.pulseProgress = (this.pulseProgress + 0.004) % 1.0;
            const pt = this.pathCurve.getPointAt(this.pulseProgress);
            this.pulseSphere.position.copy(pt);
        }

        this.controls.update();
        this.renderer.render(this.scene, this.camera);
    }
}

// Global initialization
window.addEventListener("DOMContentLoaded", () => {
    window.crime3D = new CrimeScene3D("three-canvas");
});
