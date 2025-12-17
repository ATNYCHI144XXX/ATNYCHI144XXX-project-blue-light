"""
Notification Service

Handles multi-channel alert delivery to law enforcement systems.
"""

import logging
from typing import List, Optional
from enum import Enum

from .alert_generator import AlertPacket


class NotificationChannel(Enum):
    """Available notification channels."""
    PATROL_DIRECT = "patrol_direct"  # Direct to patrol unit
    COMMAND_CENTER = "command_center"  # To command center dashboard
    DATABASE = "database"  # To permanent storage
    EMAIL = "email"  # Email notification (backup)
    

class NotificationService:
    """
    Multi-channel alert notification service.
    
    Delivers alerts to law enforcement through multiple channels including
    direct patrol unit transmission, command center dashboards, and databases.
    """
    
    def __init__(self):
        """Initialize notification service."""
        self.logger = logging.getLogger(__name__)
        self._enabled_channels = [
            NotificationChannel.PATROL_DIRECT,
            NotificationChannel.COMMAND_CENTER,
            NotificationChannel.DATABASE
        ]
        
    def send_alert(self, alert: AlertPacket, priority: int = 3) -> bool:
        """
        Send alert through all enabled channels.
        
        Args:
            alert: AlertPacket to send
            priority: Priority level (1-5, 5 being highest)
            
        Returns:
            True if alert sent successfully through at least one channel
        """
        success = False
        
        for channel in self._enabled_channels:
            try:
                if self._send_via_channel(alert, channel, priority):
                    success = True
                    self.logger.info(f"Alert {alert.alert_id} sent via {channel.value}")
                else:
                    self.logger.warning(f"Failed to send alert via {channel.value}")
            except Exception as e:
                self.logger.error(f"Error sending via {channel.value}: {e}")
                
        return success
        
    def _send_via_channel(
        self,
        alert: AlertPacket,
        channel: NotificationChannel,
        priority: int
    ) -> bool:
        """Send alert via specific channel."""
        if channel == NotificationChannel.PATROL_DIRECT:
            return self._send_to_patrol(alert, priority)
        elif channel == NotificationChannel.COMMAND_CENTER:
            return self._send_to_command_center(alert)
        elif channel == NotificationChannel.DATABASE:
            return self._send_to_database(alert)
        elif channel == NotificationChannel.EMAIL:
            return self._send_email(alert)
        else:
            return False
            
    def _send_to_patrol(self, alert: AlertPacket, priority: int) -> bool:
        """
        Send alert directly to patrol unit.
        
        Uses encrypted 5G or fiber connection for sub-100ms delivery.
        """
        # TODO: Implement direct patrol unit communication
        self.logger.info(f"[PATROL] Alert {alert.alert_id} (Priority: {priority})")
        return True
        
    def _send_to_command_center(self, alert: AlertPacket) -> bool:
        """Send alert to command center dashboard."""
        # TODO: Implement command center API call
        self.logger.info(f"[COMMAND] Alert {alert.alert_id}")
        return True
        
    def _send_to_database(self, alert: AlertPacket) -> bool:
        """Store alert in permanent database."""
        # TODO: Implement database storage
        self.logger.info(f"[DATABASE] Alert {alert.alert_id}")
        return True
        
    def _send_email(self, alert: AlertPacket) -> bool:
        """Send email notification (backup channel)."""
        # TODO: Implement email notification
        self.logger.info(f"[EMAIL] Alert {alert.alert_id}")
        return True
        
    def enable_channel(self, channel: NotificationChannel) -> None:
        """Enable a notification channel."""
        if channel not in self._enabled_channels:
            self._enabled_channels.append(channel)
            
    def disable_channel(self, channel: NotificationChannel) -> None:
        """Disable a notification channel."""
        if channel in self._enabled_channels:
            self._enabled_channels.remove(channel)
            
    def get_enabled_channels(self) -> List[NotificationChannel]:
        """Get list of enabled notification channels."""
        return self._enabled_channels.copy()
